from datetime import date

ORDERS_FILE = "database/orders.txt"

def generate_order_id():
    try:
        with open(ORDERS_FILE, "r") as f:
            lines = f.readlines()
            lines = [l for l in lines if l.strip() != ""]
        if len(lines) == 0:
            return "ORD001"
        last_line  = lines[-1].strip()
        last_id    = last_line.split("|")[0]
        number     = int(last_id[3:])
        new_number = number + 1
        return "ORD" + str(new_number).zfill(3)
    except FileNotFoundError:
        return "ORD001"

def add_order():
    print("\n" + "=" * 45)
    print("           ADD NEW ORDER")
    print("=" * 45)
    customer_name    = input("Customer Name     : ").strip()
    customer_address = input("Delivery Address  : ").strip()
    contact_number   = input("Contact Number    : ").strip()
    deadline         = input("Delivery Deadline (YYYY-MM-DD) : ").strip()
    weight           = input("Package Weight (kg)            : ").strip()
    order_id   = generate_order_id()
    order_date = str(date.today())
    status     = "Pending"
    new_record = f"{order_id}|{customer_name}|{customer_address}|{contact_number}|{order_date}|{deadline}|{weight}|{status}\n"
    with open(ORDERS_FILE, "a") as f:
        f.write(new_record)
    print(f"\nOrder {order_id} added successfully!")
    print(f"Status set to: Pending")

def view_orders():
    print("\n" + "=" * 75)
    print("                        ALL ORDERS")
    print("=" * 75)
    try:
        with open(ORDERS_FILE, "r") as f:
            lines = f.readlines()
            lines = [l for l in lines if l.strip() != ""]
        if len(lines) == 0:
            print("No orders found.")
            return
        print(f"{'ID':<8} {'Customer':<15} {'Contact':<12} {'Deadline':<12} {'Weight':<8} {'Status'}")
        print("-" * 75)
        for line in lines:
            fields = line.strip().split("|")
            print(f"{fields[0]:<8} {fields[1]:<15} {fields[3]:<12} {fields[5]:<12} {fields[6]:<8} {fields[7]}")
        print("-" * 75)
        print(f"Total Orders: {len(lines)}")
    except FileNotFoundError:
        print("No orders file found.")

def search_order():
    print("\n" + "=" * 45)
    print("            SEARCH ORDER")
    print("=" * 45)
    search = input("Enter Order ID or Customer Name : ").strip().lower()
    found = False
    try:
        with open(ORDERS_FILE, "r") as f:
            for line in f:
                if line.strip() == "":
                    continue
                if search in line.lower():
                    fields = line.strip().split("|")
                    print("\n" + "-" * 45)
                    print(f"  Order ID   : {fields[0]}")
                    print(f"  Customer   : {fields[1]}")
                    print(f"  Address    : {fields[2]}")
                    print(f"  Contact    : {fields[3]}")
                    print(f"  Order Date : {fields[4]}")
                    print(f"  Deadline   : {fields[5]}")
                    print(f"  Weight     : {fields[6]} kg")
                    print(f"  Status     : {fields[7]}")
                    print("-" * 45)
                    found = True
        if not found:
            print(f"\nNo orders found matching: {search}")
    except FileNotFoundError:
        print("No orders file found.")

def update_order():
    print("\n" + "=" * 45)
    print("            UPDATE ORDER")
    print("=" * 45)
    order_id = input("Enter Order ID to update : ").strip().upper()
    try:
        with open(ORDERS_FILE, "r") as f:
            lines = f.readlines()
        found = False
        for i in range(len(lines)):
            if lines[i].strip() == "":
                continue
            fields = lines[i].strip().split("|")
            if fields[0] == order_id:
                found = True
                print(f"\nCurrent Details:")
                print(f"  1. Address   : {fields[2]}")
                print(f"  2. Contact   : {fields[3]}")
                print(f"  3. Deadline  : {fields[5]}")
                print(f"  4. Weight    : {fields[6]}")
                print("\nWhat do you want to update?")
                print("  1. Address")
                print("  2. Contact Number")
                print("  3. Deadline")
                print("  4. Weight")
                choice = input("Enter choice : ").strip()
                if choice == "1":
                    fields[2] = input("New Address  : ").strip()
                elif choice == "2":
                    fields[3] = input("New Contact  : ").strip()
                elif choice == "3":
                    fields[5] = input("New Deadline : ").strip()
                elif choice == "4":
                    fields[6] = input("New Weight   : ").strip()
                else:
                    print("Invalid choice.")
                    return
                lines[i] = "|".join(fields) + "\n"
                with open(ORDERS_FILE, "w") as f:
                    f.writelines(lines)
                print(f"\nOrder {order_id} updated successfully!")
                break
        if not found:
            print(f"\nOrder {order_id} not found.")
    except FileNotFoundError:
        print("No orders file found.")

def cancel_order():
    print("\n" + "=" * 45)
    print("            CANCEL ORDER")
    print("=" * 45)
    order_id = input("Enter Order ID to cancel : ").strip().upper()
    try:
        with open(ORDERS_FILE, "r") as f:
            lines = f.readlines()
        found = False
        for i in range(len(lines)):
            if lines[i].strip() == "":
                continue
            fields = lines[i].strip().split("|")
            if fields[0] == order_id:
                found = True
                current_status = fields[7]
                if current_status == "Delivered":
                    print("\nCannot cancel. Order already delivered.")
                    return
                if current_status == "Cancelled":
                    print("\nOrder is already cancelled.")
                    return
                confirm = input(f"\nCancel order {order_id}? (yes/no) : ").strip().lower()
                if confirm == "yes":
                    fields[7] = "Cancelled"
                    lines[i]  = "|".join(fields) + "\n"
                    with open(ORDERS_FILE, "w") as f:
                        f.writelines(lines)
                    print(f"\nOrder {order_id} cancelled successfully!")
                else:
                    print("\nCancellation aborted.")
                break
        if not found:
            print(f"\nOrder {order_id} not found.")
    except FileNotFoundError:
        print("No orders file found.")

def order_management_menu():
    while True:
        print("\n" + "=" * 45)
        print("          ORDER MANAGEMENT")
        print("=" * 45)
        print("  1. Add New Order")
        print("  2. View All Orders")
        print("  3. Search Order")
        print("  4. Update Order")
        print("  5. Cancel Order")
        print("  6. Back to Admin Menu")
        print("=" * 45)
        choice = input("Enter choice : ").strip()
        if choice == "1":
            add_order()
        elif choice == "2":
            view_orders()
        elif choice == "3":
            search_order()
        elif choice == "4":
            update_order()
        elif choice == "5":
            cancel_order()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please enter 1-6.")
            

