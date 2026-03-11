# ============================================
#   delivery_tracking.py
# ============================================

ORDERS_FILE = "database/orders.txt"
ROUTES_FILE = "database/routes.txt"

STATUS_FLOW = {
    "Assigned"        : "Picked Up",
    "Picked Up"       : "Out for Delivery",
    "Out for Delivery": "Delivered"
}


def get_driver_orders(driver_id):
    driver_orders = []
    try:
        # Find all routes for this driver
        with open(ROUTES_FILE, "r") as f:
            routes = [l.strip() for l in f if l.strip() != ""]

        for route in routes:
            fields = route.split("|")
            if fields[2] == driver_id and fields[6] == "Active":
                driver_orders.append(fields[1])

        return driver_orders

    except FileNotFoundError:
        return []


def view_my_orders(driver_id):
    print("\n" + "=" * 60)
    print("            MY ASSIGNED ORDERS")
    print("=" * 60)

    order_ids = get_driver_orders(driver_id)

    if len(order_ids) == 0:
        print("No active orders assigned to you.")
        return

    try:
        with open(ORDERS_FILE, "r") as f:
            orders = [l.strip() for l in f if l.strip() != ""]

        print(f"{'ID':<8} {'Customer':<15} {'Address':<20} {'Deadline':<12} {'Status'}")
        print("-" * 60)

        found = False
        for order in orders:
            fields = order.split("|")
            if fields[0] in order_ids:
                print(f"{fields[0]:<8} {fields[1]:<15} {fields[2]:<20} {fields[5]:<12} {fields[7]}")
                found = True

        if not found:
            print("No orders found.")

        print("-" * 60)

    except FileNotFoundError:
        print("Orders file not found.")


def update_delivery_status(driver_id):
    print("\n" + "=" * 45)
    print("       UPDATE DELIVERY STATUS")
    print("=" * 45)

    order_ids = get_driver_orders(driver_id)

    if len(order_ids) == 0:
        print("No active orders assigned to you.")
        return

    order_id = input("Enter Order ID : ").strip().upper()

    if order_id not in order_ids:
        print(f"\nOrder {order_id} is not assigned to you.")
        return

    try:
        with open(ORDERS_FILE, "r") as f:
            lines = f.readlines()

        found = False
        for i in range(len(lines)):
            if lines[i].strip() == "":
                continue
            fields = lines[i].strip().split("|")
            if fields[0] == order_id:
                found      = True
                cur_status = fields[7]

                if cur_status == "Delivered":
                    print("\nOrder already delivered.")
                    return

                if cur_status not in STATUS_FLOW:
                    print(f"\nCannot update from status: {cur_status}")
                    return

                next_status = STATUS_FLOW[cur_status]
                print(f"\nCurrent Status : {cur_status}")
                print(f"Next Status    : {next_status}")

                confirm = input("\nConfirm update? (yes/no) : ").strip().lower()

                if confirm == "yes":
                    fields[7] = next_status
                    lines[i]  = "|".join(fields) + "\n"

                    with open(ORDERS_FILE, "w") as f:
                        f.writelines(lines)

                    print(f"\nOrder {order_id} updated to: {next_status}")
                else:
                    print("\nUpdate cancelled.")
                break

        if not found:
            print(f"\nOrder {order_id} not found.")

    except FileNotFoundError:
        print("Orders file not found.")


def view_my_performance(driver_id):
    print("\n" + "=" * 45)
    print("          MY PERFORMANCE")
    print("=" * 45)

    total     = 0
    completed = 0
    active    = 0

    try:
        with open(ROUTES_FILE, "r") as f:
            routes = [l.strip() for l in f if l.strip() != ""]

        for route in routes:
            fields = route.split("|")
            if fields[2] == driver_id:
                total += 1
                if fields[6] == "Completed":
                    completed += 1
                elif fields[6] == "Active":
                    active += 1

        rate = round((completed / total) * 100, 1) if total > 0 else 0.0

        print(f"\n  Driver ID        : {driver_id}")
        print(f"  Total Routes     : {total}")
        print(f"  Completed        : {completed}")
        print(f"  Active           : {active}")
        print(f"  Success Rate     : {rate}%")
        print("=" * 45)

    except FileNotFoundError:
        print("Routes file not found.")