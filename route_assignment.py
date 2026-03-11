# ============================================
#   route_assignment.py
# ============================================

ROUTES_FILE  = "database/routes.txt"
ORDERS_FILE  = "database/orders.txt"
DRIVERS_FILE = "database/drivers.txt"
VEHICLES_FILE = "database/vehicles.txt"


# ============================================
#   HELPER - Generate Route ID
# ============================================

def generate_route_id():
    try:
        with open(ROUTES_FILE, "r") as f:
            lines = f.readlines()
            lines = [l for l in lines if l.strip() != ""]
        if len(lines) == 0:
            return "RTE001"
        last_id    = lines[-1].strip().split("|")[0]
        number     = int(last_id[3:])
        new_number = number + 1
        return "RTE" + str(new_number).zfill(3)
    except FileNotFoundError:
        return "RTE001"


# ============================================
#   HELPER - Check Order
# ============================================

def check_order(order_id):
    try:
        with open(ORDERS_FILE, "r") as f:
            for line in f:
                if line.strip() == "":
                    continue
                fields = line.strip().split("|")
                if fields[0] == order_id:
                    return fields
        return None
    except FileNotFoundError:
        return None


# ============================================
#   HELPER - Check Driver
# ============================================

def check_driver(driver_id):
    try:
        with open(DRIVERS_FILE, "r") as f:
            for line in f:
                if line.strip() == "":
                    continue
                fields = line.strip().split("|")
                if fields[0] == driver_id:
                    return fields
        return None
    except FileNotFoundError:
        return None


# ============================================
#   HELPER - Check Vehicle
# ============================================

def check_vehicle(vehicle_id):
    try:
        with open(VEHICLES_FILE, "r") as f:
            for line in f:
                if line.strip() == "":
                    continue
                fields = line.strip().split("|")
                if fields[0] == vehicle_id:
                    return fields
        return None
    except FileNotFoundError:
        return None


# ============================================
#   HELPER - Update A Record In Any File
# ============================================

def update_record(filepath, record_id, field_index, new_value):
    with open(filepath, "r") as f:
        lines = f.readlines()
    for i in range(len(lines)):
        if lines[i].strip() == "":
            continue
        fields = lines[i].strip().split("|")
        if fields[0] == record_id:
            fields[field_index] = new_value
            lines[i] = "|".join(fields) + "\n"
            break
    with open(filepath, "w") as f:
        f.writelines(lines)


# ============================================
#   FUNCTION 1 - Assign Route
# ============================================

def assign_route():
    print("\n" + "=" * 45)
    print("          ASSIGN ROUTE")
    print("=" * 45)

    order_id  = input("Enter Order ID   : ").strip().upper()
    driver_id = input("Enter Driver ID  : ").strip().upper()
    vehicle_id = input("Enter Vehicle ID : ").strip().upper()

    # Check order
    order = check_order(order_id)
    if order is None:
        print(f"\nOrder {order_id} not found.")
        return
    if order[7] != "Pending":
        print(f"\nOrder {order_id} is not Pending.")
        print(f"Current status: {order[7]}")
        return

    # Check driver
    driver = check_driver(driver_id)
    if driver is None:
        print(f"\nDriver {driver_id} not found.")
        return
    if driver[5] != "Available":
        print(f"\nDriver {driver_id} is not Available.")
        print(f"Current status: {driver[5]}")
        return

    # Check vehicle
    vehicle = check_vehicle(vehicle_id)
    if vehicle is None:
        print(f"\nVehicle {vehicle_id} not found.")
        return
    if vehicle[5] != "Good":
        print(f"\nVehicle {vehicle_id} is not available.")
        print(f"Current status: {vehicle[5]}")
        return

    # All checks passed
    distance  = input("Distance (km)          : ").strip()
    est_time  = input("Estimated Delivery Time: ").strip()
    route_id  = generate_route_id()
    status    = "Active"

    # Write to routes.txt
    new_record = f"{route_id}|{order_id}|{driver_id}|{vehicle_id}|{distance}|{est_time}|{status}\n"
    with open(ROUTES_FILE, "a") as f:
        f.write(new_record)

    # Update order status → Assigned
    update_record(ORDERS_FILE, order_id, 7, "Assigned")

    # Update driver status → On Duty
    update_record(DRIVERS_FILE, driver_id, 5, "On Duty")

    print(f"\nRoute {route_id} assigned successfully!")
    print(f"  Order  {order_id}  → Assigned")
    print(f"  Driver {driver_id} → On Duty")


# ============================================
#   FUNCTION 2 - View Active Routes
# ============================================

def view_active_routes():
    print("\n" + "=" * 75)
    print("                      ACTIVE ROUTES")
    print("=" * 75)
    try:
        with open(ROUTES_FILE, "r") as f:
            lines = f.readlines()
            lines = [l for l in lines if l.strip() != ""]

        active = [l for l in lines if l.strip().split("|")[6] == "Active"]

        if len(active) == 0:
            print("No active routes found.")
            return

        print(f"{'Route':<8} {'Order':<8} {'Driver':<8} {'Vehicle':<8} {'Distance':<10} {'Est.Time':<10} {'Status'}")
        print("-" * 75)
        for line in active:
            fields = line.strip().split("|")
            print(f"{fields[0]:<8} {fields[1]:<8} {fields[2]:<8} {fields[3]:<8} {fields[4]:<10} {fields[5]:<10} {fields[6]}")
        print("-" * 75)
        print(f"Total Active Routes: {len(active)}")

    except FileNotFoundError:
        print("No routes file found.")


# ============================================
#   FUNCTION 3 - View All Routes
# ============================================

def view_all_routes():
    print("\n" + "=" * 75)
    print("                       ALL ROUTES")
    print("=" * 75)
    try:
        with open(ROUTES_FILE, "r") as f:
            lines = f.readlines()
            lines = [l for l in lines if l.strip() != ""]

        if len(lines) == 0:
            print("No routes found.")
            return

        print(f"{'Route':<8} {'Order':<8} {'Driver':<8} {'Vehicle':<8} {'Distance':<10} {'Est.Time':<10} {'Status'}")
        print("-" * 75)
        for line in lines:
            fields = line.strip().split("|")
            print(f"{fields[0]:<8} {fields[1]:<8} {fields[2]:<8} {fields[3]:<8} {fields[4]:<10} {fields[5]:<10} {fields[6]}")
        print("-" * 75)
        print(f"Total Routes: {len(lines)}")

    except FileNotFoundError:
        print("No routes file found.")


# ============================================
#   FUNCTION 4 - Complete Route
# ============================================

def complete_route():
    print("\n" + "=" * 45)
    print("         COMPLETE ROUTE")
    print("=" * 45)

    route_id = input("Enter Route ID to complete : ").strip().upper()

    try:
        with open(ROUTES_FILE, "r") as f:
            lines = f.readlines()

        found = False

        for i in range(len(lines)):
            if lines[i].strip() == "":
                continue
            fields = lines[i].strip().split("|")

            if fields[0] == route_id:
                found = True

                if fields[6] == "Completed":
                    print("\nRoute already completed.")
                    return

                if fields[6] != "Active":
                    print(f"\nRoute status is: {fields[6]}")
                    print("Only Active routes can be completed.")
                    return

                order_id  = fields[1]
                driver_id = fields[2]

                confirm = input(f"\nComplete route {route_id}? (yes/no) : ").strip().lower()

                if confirm == "yes":
                    # Update route status
                    fields[6] = "Completed"
                    lines[i]  = "|".join(fields) + "\n"
                    with open(ROUTES_FILE, "w") as f:
                        f.writelines(lines)

                    # Update order → Delivered
                    update_record(ORDERS_FILE, order_id, 7, "Delivered")

                    # Update driver → Available
                    update_record(DRIVERS_FILE, driver_id, 5, "Available")

                    print(f"\nRoute {route_id} completed!")
                    print(f"  Order  {order_id}  → Delivered")
                    print(f"  Driver {driver_id} → Available")
                else:
                    print("\nCancelled.")
                break

        if not found:
            print(f"\nRoute {route_id} not found.")

    except FileNotFoundError:
        print("No routes file found.")


# ============================================
#   ROUTE ASSIGNMENT MENU
# ============================================

def route_assignment_menu():
    while True:
        print("\n" + "=" * 45)
        print("         ROUTE ASSIGNMENT")
        print("=" * 45)
        print("  1. Assign Route")
        print("  2. View Active Routes")
        print("  3. View All Routes")
        print("  4. Complete Route")
        print("  5. Back to Admin Menu")
        print("=" * 45)
        choice = input("Enter choice : ").strip()
        if choice == "1":
            assign_route()
        elif choice == "2":
            view_active_routes()
        elif choice == "3":
            view_all_routes()
        elif choice == "4":
            complete_route()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please enter 1-5.")