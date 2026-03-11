# ============================================
#   reports.py
# ============================================

ORDERS_FILE  = "database/orders.txt"
DRIVERS_FILE = "database/drivers.txt"
VEHICLES_FILE = "database/vehicles.txt"
ROUTES_FILE  = "database/routes.txt"
FUEL_FILE    = "database/fuel_records.txt"


# ============================================
#   REPORT 1 - Driver Performance Report
# ============================================

def driver_performance_report():
    print("\n" + "=" * 55)
    print("          DRIVER PERFORMANCE REPORT")
    print("=" * 55)

    try:
        # Read all drivers
        with open(DRIVERS_FILE, "r") as f:
            drivers = [l.strip() for l in f if l.strip() != ""]

        # Read all routes
        with open(ROUTES_FILE, "r") as f:
            routes = [l.strip() for l in f if l.strip() != ""]

        if len(drivers) == 0:
            print("No drivers found.")
            return

        print(f"\n{'Driver':<8} {'Name':<15} {'Total':<8} {'Done':<8} {'Failed':<8} {'Rate'}")
        print("-" * 55)

        for driver_line in drivers:
            driver_fields = driver_line.split("|")
            driver_id     = driver_fields[0]
            driver_name   = driver_fields[1]
            driver_status = driver_fields[5]

            if driver_status == "Removed":
                continue

            total     = 0
            completed = 0
            failed    = 0

            for route_line in routes:
                route_fields = route_line.split("|")
                if route_fields[2] == driver_id:
                    total += 1
                    if route_fields[6] == "Completed":
                        completed += 1
                    elif route_fields[6] == "Failed":
                        failed += 1

            if total > 0:
                rate = round((completed / total) * 100, 1)
            else:
                rate = 0.0

            print(f"{driver_id:<8} {driver_name:<15} {total:<8} {completed:<8} {failed:<8} {rate}%")

        print("-" * 55)

    except FileNotFoundError:
        print("Required files not found.")


# ============================================
#   REPORT 2 - Vehicle Performance Report
# ============================================

def vehicle_performance_report():
    print("\n" + "=" * 60)
    print("          VEHICLE PERFORMANCE REPORT")
    print("=" * 60)

    try:
        with open(VEHICLES_FILE, "r") as f:
            vehicles = [l.strip() for l in f if l.strip() != ""]

        with open(ROUTES_FILE, "r") as f:
            routes = [l.strip() for l in f if l.strip() != ""]

        with open(FUEL_FILE, "r") as f:
            fuel_records = [l.strip() for l in f if l.strip() != ""]

        if len(vehicles) == 0:
            print("No vehicles found.")
            return

        print(f"\n{'Vehicle':<8} {'Type':<8} {'Routes':<8} {'Fuel(L)':<10} {'Cost':<10} {'Status'}")
        print("-" * 60)

        for v_line in vehicles:
            v_fields   = v_line.split("|")
            v_id       = v_fields[0]
            v_type     = v_fields[1]
            v_status   = v_fields[5]

            total_routes = 0
            total_fuel   = 0.0
            total_cost   = 0.0

            for route_line in routes:
                route_fields = route_line.split("|")
                if route_fields[3] == v_id:
                    total_routes += 1

            for fuel_line in fuel_records:
                fuel_fields = fuel_line.split("|")
                if fuel_fields[2] == v_id:
                    total_fuel += float(fuel_fields[3])
                    total_cost += float(fuel_fields[4])

            print(f"{v_id:<8} {v_type:<8} {total_routes:<8} {total_fuel:<10} {total_cost:<10} {v_status}")

        print("-" * 60)

    except FileNotFoundError:
        print("Required files not found.")


# ============================================
#   REPORT 3 - Operational Summary
# ============================================

def operational_summary():
    print("\n" + "=" * 45)
    print("        OPERATIONAL SUMMARY")
    print("=" * 45)

    try:
        # Orders summary
        with open(ORDERS_FILE, "r") as f:
            orders = [l.strip() for l in f if l.strip() != ""]

        total_orders    = 0
        pending_orders  = 0
        assigned_orders = 0
        delivered_orders= 0
        cancelled_orders= 0

        for order in orders:
            fields = order.split("|")
            total_orders += 1
            status = fields[7]
            if status == "Pending":
                pending_orders += 1
            elif status == "Assigned":
                assigned_orders += 1
            elif status == "Delivered":
                delivered_orders += 1
            elif status == "Cancelled":
                cancelled_orders += 1

        # Drivers summary
        with open(DRIVERS_FILE, "r") as f:
            drivers = [l.strip() for l in f if l.strip() != ""]

        total_drivers     = 0
        available_drivers = 0
        on_duty_drivers   = 0

        for driver in drivers:
            fields = driver.split("|")
            if fields[5] != "Removed":
                total_drivers += 1
                if fields[5] == "Available":
                    available_drivers += 1
                elif fields[5] == "On Duty":
                    on_duty_drivers += 1

        # Fuel summary
        with open(FUEL_FILE, "r") as f:
            fuel_records = [l.strip() for l in f if l.strip() != ""]

        total_fuel_cost = 0.0
        for record in fuel_records:
            fields = record.split("|")
            total_fuel_cost += float(fields[4])

        # Routes summary
        with open(ROUTES_FILE, "r") as f:
            routes = [l.strip() for l in f if l.strip() != ""]

        active_routes    = len([r for r in routes if r.split("|")[6] == "Active"])
        completed_routes = len([r for r in routes if r.split("|")[6] == "Completed"])

        # Print summary
        print("\n  --- ORDERS ---")
        print(f"  Total Orders     : {total_orders}")
        print(f"  Pending          : {pending_orders}")
        print(f"  Assigned         : {assigned_orders}")
        print(f"  Delivered        : {delivered_orders}")
        print(f"  Cancelled        : {cancelled_orders}")

        print("\n  --- DRIVERS ---")
        print(f"  Total Drivers    : {total_drivers}")
        print(f"  Available        : {available_drivers}")
        print(f"  On Duty          : {on_duty_drivers}")

        print("\n  --- ROUTES ---")
        print(f"  Active Routes    : {active_routes}")
        print(f"  Completed Routes : {completed_routes}")

        print("\n  --- FINANCIALS ---")
        print(f"  Total Fuel Cost  : {total_fuel_cost}")

        print("\n" + "=" * 45)

    except FileNotFoundError:
        print("Required files not found.")


# ============================================
#   REPORTS MENU
# ============================================

def reports_menu():
    while True:
        print("\n" + "=" * 45)
        print("             REPORTS")
        print("=" * 45)
        print("  1. Driver Performance Report")
        print("  2. Vehicle Performance Report")
        print("  3. Operational Summary")
        print("  4. Back")
        print("=" * 45)
        choice = input("Enter choice : ").strip()
        if choice == "1":
            driver_performance_report()
        elif choice == "2":
            vehicle_performance_report()
        elif choice == "3":
            operational_summary()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please enter 1-4.")