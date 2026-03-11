# ============================================
#   fuel_tracking.py
# ============================================

from datetime import date

FUEL_FILE    = "database/fuel_records.txt"
DRIVERS_FILE = "database/drivers.txt"
VEHICLES_FILE = "database/vehicles.txt"
ROUTES_FILE  = "database/routes.txt"


# ============================================
#   HELPER - Generate Fuel Record ID
# ============================================

def generate_fuel_id():
    try:
        with open(FUEL_FILE, "r") as f:
            lines = f.readlines()
            lines = [l for l in lines if l.strip() != ""]
        if len(lines) == 0:
            return "FUEL001"
        last_id    = lines[-1].strip().split("|")[0]
        number     = int(last_id[4:])
        new_number = number + 1
        return "FUEL" + str(new_number).zfill(3)
    except FileNotFoundError:
        return "FUEL001"


# ============================================
#   HELPER - Check If Driver Exists
# ============================================

def driver_exists(driver_id):
    try:
        with open(DRIVERS_FILE, "r") as f:
            for line in f:
                if line.strip() == "":
                    continue
                if line.strip().split("|")[0] == driver_id:
                    return True
        return False
    except FileNotFoundError:
        return False


# ============================================
#   HELPER - Check If Vehicle Exists
# ============================================

def vehicle_exists(vehicle_id):
    try:
        with open(VEHICLES_FILE, "r") as f:
            for line in f:
                if line.strip() == "":
                    continue
                if line.strip().split("|")[0] == vehicle_id:
                    return True
        return False
    except FileNotFoundError:
        return False


# ============================================
#   FUNCTION 1 - Add Fuel Record
# ============================================

def add_fuel_record():
    print("\n" + "=" * 45)
    print("          ADD FUEL RECORD")
    print("=" * 45)

    driver_id  = input("Driver ID        : ").strip().upper()
    vehicle_id = input("Vehicle ID       : ").strip().upper()
    route_id   = input("Route ID         : ").strip().upper()

    # Validate driver
    if not driver_exists(driver_id):
        print(f"\nDriver {driver_id} not found.")
        return

    # Validate vehicle
    if not vehicle_exists(vehicle_id):
        print(f"\nVehicle {vehicle_id} not found.")
        return

    fuel_qty  = input("Fuel Quantity (L): ").strip()
    fuel_cost = input("Fuel Cost        : ").strip()

    fuel_id    = generate_fuel_id()
    today      = str(date.today())

    new_record = f"{fuel_id}|{driver_id}|{vehicle_id}|{fuel_qty}|{fuel_cost}|{today}|{route_id}\n"

    with open(FUEL_FILE, "a") as f:
        f.write(new_record)

    print(f"\nFuel record {fuel_id} added successfully!")
    print(f"  Driver  : {driver_id}")
    print(f"  Vehicle : {vehicle_id}")
    print(f"  Fuel    : {fuel_qty} L")
    print(f"  Cost    : {fuel_cost}")
    print(f"  Date    : {today}")


# ============================================
#   FUNCTION 2 - View All Fuel Records
# ============================================

def view_fuel_records():
    print("\n" + "=" * 80)
    print("                      ALL FUEL RECORDS")
    print("=" * 80)

    try:
        with open(FUEL_FILE, "r") as f:
            lines = f.readlines()
            lines = [l for l in lines if l.strip() != ""]

        if len(lines) == 0:
            print("No fuel records found.")
            return

        print(f"{'ID':<10} {'Driver':<8} {'Vehicle':<8} {'Qty(L)':<8} {'Cost':<10} {'Date':<12} {'Route'}")
        print("-" * 80)

        total_cost = 0
        total_qty  = 0

        for line in lines:
            fields = line.strip().split("|")
            print(f"{fields[0]:<10} {fields[1]:<8} {fields[2]:<8} {fields[3]:<8} {fields[4]:<10} {fields[5]:<12} {fields[6]}")
            total_cost += float(fields[4])
            total_qty  += float(fields[3])

        print("-" * 80)
        print(f"Total Fuel Used : {total_qty} L")
        print(f"Total Fuel Cost : {total_cost}")

    except FileNotFoundError:
        print("No fuel records file found.")


# ============================================
#   FUNCTION 3 - Driver Fuel Report
# ============================================

def driver_fuel_report():
    print("\n" + "=" * 45)
    print("        DRIVER FUEL REPORT")
    print("=" * 45)

    driver_id = input("Enter Driver ID : ").strip().upper()

    if not driver_exists(driver_id):
        print(f"\nDriver {driver_id} not found.")
        return

    total_qty  = 0
    total_cost = 0
    trip_count = 0

    try:
        with open(FUEL_FILE, "r") as f:
            lines = f.readlines()

        print(f"\n{'ID':<10} {'Vehicle':<8} {'Qty(L)':<8} {'Cost':<10} {'Date':<12} {'Route'}")
        print("-" * 60)

        for line in lines:
            if line.strip() == "":
                continue
            fields = line.strip().split("|")
            if fields[1] == driver_id:
                print(f"{fields[0]:<10} {fields[2]:<8} {fields[3]:<8} {fields[4]:<10} {fields[5]:<12} {fields[6]}")
                total_qty  += float(fields[3])
                total_cost += float(fields[4])
                trip_count += 1

        print("-" * 60)

        if trip_count == 0:
            print(f"No fuel records found for driver {driver_id}")
        else:
            print(f"Total Trips     : {trip_count}")
            print(f"Total Fuel Used : {total_qty} L")
            print(f"Total Fuel Cost : {total_cost}")
            if trip_count > 0:
                print(f"Avg Cost/Trip   : {round(total_cost / trip_count, 2)}")

    except FileNotFoundError:
        print("No fuel records file found.")


# ============================================
#   FUNCTION 4 - Monthly Fuel Report
# ============================================

def monthly_fuel_report():
    print("\n" + "=" * 45)
    print("       MONTHLY FUEL REPORT")
    print("=" * 45)

    month = input("Enter Month (YYYY-MM) : ").strip()

    total_qty  = 0
    total_cost = 0
    trip_count = 0
    driver_costs = {}

    try:
        with open(FUEL_FILE, "r") as f:
            lines = f.readlines()

        print(f"\nFuel Records for: {month}")
        print(f"\n{'ID':<10} {'Driver':<8} {'Vehicle':<8} {'Qty(L)':<8} {'Cost':<10} {'Date'}")
        print("-" * 65)

        for line in lines:
            if line.strip() == "":
                continue
            fields = line.strip().split("|")

            # Check if record belongs to this month
            if fields[5].startswith(month):
                print(f"{fields[0]:<10} {fields[1]:<8} {fields[2]:<8} {fields[3]:<8} {fields[4]:<10} {fields[5]}")
                total_qty  += float(fields[3])
                total_cost += float(fields[4])
                trip_count += 1

                # Track per driver cost
                if fields[1] not in driver_costs:
                    driver_costs[fields[1]] = 0
                driver_costs[fields[1]] += float(fields[4])

        print("-" * 65)

        if trip_count == 0:
            print(f"No records found for month: {month}")
        else:
            print(f"Total Trips     : {trip_count}")
            print(f"Total Fuel Used : {total_qty} L")
            print(f"Total Fuel Cost : {total_cost}")

            # Find highest fuel user
            if driver_costs:
                top_driver = max(driver_costs, key=driver_costs.get)
                print(f"Top Fuel User   : {top_driver} ({driver_costs[top_driver]})")

    except FileNotFoundError:
        print("No fuel records file found.")


# ============================================
#   FUEL TRACKING MENU
# ============================================

def fuel_tracking_menu():
    while True:
        print("\n" + "=" * 45)
        print("          FUEL TRACKING")
        print("=" * 45)
        print("  1. Add Fuel Record")
        print("  2. View All Fuel Records")
        print("  3. Driver Fuel Report")
        print("  4. Monthly Fuel Report")
        print("  5. Back to Admin Menu")
        print("=" * 45)
        choice = input("Enter choice : ").strip()
        if choice == "1":
            add_fuel_record()
        elif choice == "2":
            view_fuel_records()
        elif choice == "3":
            driver_fuel_report()
        elif choice == "4":
            monthly_fuel_report()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please enter 1-5.")