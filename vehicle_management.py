# ============================================
#   vehicle_management.py
# ============================================

from datetime import date

VEHICLES_FILE = "database/vehicles.txt"


def generate_vehicle_id():
    try:
        with open(VEHICLES_FILE, "r") as f:
            lines = f.readlines()
            lines = [l for l in lines if l.strip() != ""]
        if len(lines) == 0:
            return "VH001"
        last_id    = lines[-1].strip().split("|")[0]
        number     = int(last_id[2:])
        new_number = number + 1
        return "VH" + str(new_number).zfill(3)
    except FileNotFoundError:
        return "VH001"


def add_vehicle():
    print("\n" + "=" * 45)
    print("           ADD NEW VEHICLE")
    print("=" * 45)
    print("Vehicle Type options: Bike / Van / Truck")
    v_type    = input("Vehicle Type     : ").strip()
    reg_no    = input("Registration No  : ").strip()
    fuel_type = input("Fuel Type        : ").strip()
    mileage   = input("Mileage (km/l)   : ").strip()
    location  = input("Current Location : ").strip()
    v_id      = generate_vehicle_id()
    status    = "Good"
    new_record = f"{v_id}|{v_type}|{reg_no}|{fuel_type}|{mileage}|{status}|{location}\n"
    with open(VEHICLES_FILE, "a") as f:
        f.write(new_record)
    print(f"\nVehicle {v_id} added successfully!")
    print(f"Status set to: Good")


def view_vehicles():
    print("\n" + "=" * 80)
    print("                         ALL VEHICLES")
    print("=" * 80)
    try:
        with open(VEHICLES_FILE, "r") as f:
            lines = f.readlines()
            lines = [l for l in lines if l.strip() != ""]
        if len(lines) == 0:
            print("No vehicles found.")
            return
        print(f"{'ID':<8} {'Type':<8} {'Reg No':<15} {'Fuel':<8} {'Mileage':<10} {'Status':<15} {'Location'}")
        print("-" * 80)
        for line in lines:
            fields = line.strip().split("|")
            print(f"{fields[0]:<8} {fields[1]:<8} {fields[2]:<15} {fields[3]:<8} {fields[4]:<10} {fields[5]:<15} {fields[6]}")
        print("-" * 80)
        print(f"Total Vehicles: {len(lines)}")
    except FileNotFoundError:
        print("No vehicles file found.")


def search_vehicle():
    print("\n" + "=" * 45)
    print("          SEARCH VEHICLE")
    print("=" * 45)
    search = input("Enter Vehicle ID or Reg No : ").strip().lower()
    found  = False
    try:
        with open(VEHICLES_FILE, "r") as f:
            for line in f:
                if line.strip() == "":
                    continue
                if search in line.lower():
                    fields = line.strip().split("|")
                    print("\n" + "-" * 45)
                    print(f"  Vehicle ID   : {fields[0]}")
                    print(f"  Type         : {fields[1]}")
                    print(f"  Reg Number   : {fields[2]}")
                    print(f"  Fuel Type    : {fields[3]}")
                    print(f"  Mileage      : {fields[4]} km/l")
                    print(f"  Status       : {fields[5]}")
                    print(f"  Location     : {fields[6]}")
                    print("-" * 45)
                    found = True
        if not found:
            print(f"\nNo vehicles found matching: {search}")
    except FileNotFoundError:
        print("No vehicles file found.")


def update_vehicle():
    print("\n" + "=" * 45)
    print("          UPDATE VEHICLE")
    print("=" * 45)
    v_id = input("Enter Vehicle ID to update : ").strip().upper()
    try:
        with open(VEHICLES_FILE, "r") as f:
            lines = f.readlines()
        found = False
        for i in range(len(lines)):
            if lines[i].strip() == "":
                continue
            fields = lines[i].strip().split("|")
            if fields[0] == v_id:
                found = True
                print(f"\nCurrent Details:")
                print(f"  1. Mileage   : {fields[4]}")
                print(f"  2. Status    : {fields[5]}")
                print(f"  3. Location  : {fields[6]}")
                print("\nWhat do you want to update?")
                print("  1. Mileage")
                print("  2. Status")
                print("  3. Location")
                choice = input("Enter choice : ").strip()
                if choice == "1":
                    fields[4] = input("New Mileage  : ").strip()
                elif choice == "2":
                    print("Status options: Good / Under Maintenance / Out of Service")
                    fields[5] = input("New Status   : ").strip()
                elif choice == "3":
                    fields[6] = input("New Location : ").strip()
                else:
                    print("Invalid choice.")
                    return
                lines[i] = "|".join(fields) + "\n"
                with open(VEHICLES_FILE, "w") as f:
                    f.writelines(lines)
                print(f"\nVehicle {v_id} updated successfully!")
                break
        if not found:
            print(f"\nVehicle {v_id} not found.")
    except FileNotFoundError:
        print("No vehicles file found.")


def maintenance_record():
    print("\n" + "=" * 45)
    print("        VEHICLE MAINTENANCE")
    print("=" * 45)
    v_id = input("Enter Vehicle ID : ").strip().upper()
    try:
        with open(VEHICLES_FILE, "r") as f:
            lines = f.readlines()
        found = False
        for i in range(len(lines)):
            if lines[i].strip() == "":
                continue
            fields = lines[i].strip().split("|")
            if fields[0] == v_id:
                found = True
                print(f"\nVehicle  : {fields[1]} ({fields[2]})")
                print(f"Current Status : {fields[5]}")
                print("\n  1. Send to Maintenance")
                print("  2. Mark as Good (maintenance done)")
                choice = input("Enter choice : ").strip()
                if choice == "1":
                    fields[5] = "Under Maintenance"
                    print(f"\nVehicle {v_id} sent to maintenance.")
                    print(f"Date: {date.today()}")
                elif choice == "2":
                    fields[5] = "Good"
                    print(f"\nVehicle {v_id} marked as Good.")
                else:
                    print("Invalid choice.")
                    return
                lines[i] = "|".join(fields) + "\n"
                with open(VEHICLES_FILE, "w") as f:
                    f.writelines(lines)
                break
        if not found:
            print(f"\nVehicle {v_id} not found.")
    except FileNotFoundError:
        print("No vehicles file found.")


def vehicle_management_menu():
    while True:
        print("\n" + "=" * 45)
        print("        VEHICLE MANAGEMENT")
        print("=" * 45)
        print("  1. Add New Vehicle")
        print("  2. View All Vehicles")
        print("  3. Search Vehicle")
        print("  4. Update Vehicle")
        print("  5. Maintenance Record")
        print("  6. Back to Admin Menu")
        print("=" * 45)
        choice = input("Enter choice : ").strip()
        if choice == "1":
            add_vehicle()
        elif choice == "2":
            view_vehicles()
        elif choice == "3":
            search_vehicle()
        elif choice == "4":
            update_vehicle()
        elif choice == "5":
            maintenance_record()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please enter 1-6.")