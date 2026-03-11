# ============================================
#   driver_management.py
# ============================================

DRIVERS_FILE = "database/drivers.txt"


def generate_driver_id():
    try:
        with open(DRIVERS_FILE, "r") as f:
            lines = f.readlines()
            lines = [l for l in lines if l.strip() != ""]
        if len(lines) == 0:
            return "DRV001"
        last_id    = lines[-1].strip().split("|")[0]
        number     = int(last_id[3:])
        new_number = number + 1
        return "DRV" + str(new_number).zfill(3)
    except FileNotFoundError:
        return "DRV001"


def add_driver():
    print("\n" + "=" * 45)
    print("            ADD NEW DRIVER")
    print("=" * 45)
    name        = input("Driver Name      : ").strip()
    phone       = input("Phone Number     : ").strip()
    license_no  = input("License Number   : ").strip()
    vehicle_id  = input("Vehicle ID       : ").strip()
    driver_id   = generate_driver_id()
    status      = "Available"
    rating      = "0.0"
    new_record  = f"{driver_id}|{name}|{phone}|{license_no}|{vehicle_id}|{status}|{rating}\n"
    with open(DRIVERS_FILE, "a") as f:
        f.write(new_record)
    print(f"\nDriver {driver_id} added successfully!")
    print(f"Status set to: Available")


def view_drivers():
    print("\n" + "=" * 75)
    print("                        ALL DRIVERS")
    print("=" * 75)
    try:
        with open(DRIVERS_FILE, "r") as f:
            lines = f.readlines()
            lines = [l for l in lines if l.strip() != ""]
        if len(lines) == 0:
            print("No drivers found.")
            return
        print(f"{'ID':<8} {'Name':<15} {'Phone':<12} {'License':<12} {'Vehicle':<8} {'Status':<12} {'Rating'}")
        print("-" * 75)
        for line in lines:
            fields = line.strip().split("|")
            print(f"{fields[0]:<8} {fields[1]:<15} {fields[2]:<12} {fields[3]:<12} {fields[4]:<8} {fields[5]:<12} {fields[6]}")
        print("-" * 75)
        print(f"Total Drivers: {len(lines)}")
    except FileNotFoundError:
        print("No drivers file found.")


def search_driver():
    print("\n" + "=" * 45)
    print("           SEARCH DRIVER")
    print("=" * 45)
    search = input("Enter Driver ID or Name : ").strip().lower()
    found  = False
    try:
        with open(DRIVERS_FILE, "r") as f:
            for line in f:
                if line.strip() == "":
                    continue
                if search in line.lower():
                    fields = line.strip().split("|")
                    print("\n" + "-" * 45)
                    print(f"  Driver ID  : {fields[0]}")
                    print(f"  Name       : {fields[1]}")
                    print(f"  Phone      : {fields[2]}")
                    print(f"  License    : {fields[3]}")
                    print(f"  Vehicle    : {fields[4]}")
                    print(f"  Status     : {fields[5]}")
                    print(f"  Rating     : {fields[6]}")
                    print("-" * 45)
                    found = True
        if not found:
            print(f"\nNo drivers found matching: {search}")
    except FileNotFoundError:
        print("No drivers file found.")


def update_driver():
    print("\n" + "=" * 45)
    print("           UPDATE DRIVER")
    print("=" * 45)
    driver_id = input("Enter Driver ID to update : ").strip().upper()
    try:
        with open(DRIVERS_FILE, "r") as f:
            lines = f.readlines()
        found = False
        for i in range(len(lines)):
            if lines[i].strip() == "":
                continue
            fields = lines[i].strip().split("|")
            if fields[0] == driver_id:
                found = True
                print(f"\nCurrent Details:")
                print(f"  1. Phone     : {fields[2]}")
                print(f"  2. License   : {fields[3]}")
                print(f"  3. Vehicle   : {fields[4]}")
                print(f"  4. Status    : {fields[5]}")
                print(f"  5. Rating    : {fields[6]}")
                print("\nWhat do you want to update?")
                print("  1. Phone")
                print("  2. License Number")
                print("  3. Vehicle ID")
                print("  4. Status")
                print("  5. Rating")
                choice = input("Enter choice : ").strip()
                if choice == "1":
                    fields[2] = input("New Phone    : ").strip()
                elif choice == "2":
                    fields[3] = input("New License  : ").strip()
                elif choice == "3":
                    fields[4] = input("New Vehicle  : ").strip()
                elif choice == "4":
                    print("Status options: Available / On Duty / Leave")
                    fields[5] = input("New Status   : ").strip()
                elif choice == "5":
                    fields[6] = input("New Rating   : ").strip()
                else:
                    print("Invalid choice.")
                    return
                lines[i] = "|".join(fields) + "\n"
                with open(DRIVERS_FILE, "w") as f:
                    f.writelines(lines)
                print(f"\nDriver {driver_id} updated successfully!")
                break
        if not found:
            print(f"\nDriver {driver_id} not found.")
    except FileNotFoundError:
        print("No drivers file found.")


def remove_driver():
    print("\n" + "=" * 45)
    print("           REMOVE DRIVER")
    print("=" * 45)
    driver_id = input("Enter Driver ID to remove : ").strip().upper()
    try:
        with open(DRIVERS_FILE, "r") as f:
            lines = f.readlines()
        found = False
        for i in range(len(lines)):
            if lines[i].strip() == "":
                continue
            fields = lines[i].strip().split("|")
            if fields[0] == driver_id:
                found = True
                print(f"\nDriver Found: {fields[1]}")
                confirm = input(f"Remove driver {driver_id}? (yes/no) : ").strip().lower()
                if confirm == "yes":
                    fields[5] = "Removed"
                    lines[i]  = "|".join(fields) + "\n"
                    with open(DRIVERS_FILE, "w") as f:
                        f.writelines(lines)
                    print(f"\nDriver {driver_id} removed successfully!")
                else:
                    print("\nRemoval aborted.")
                break
        if not found:
            print(f"\nDriver {driver_id} not found.")
    except FileNotFoundError:
        print("No drivers file found.")


def driver_management_menu():
    while True:
        print("\n" + "=" * 45)
        print("         DRIVER MANAGEMENT")
        print("=" * 45)
        print("  1. Add New Driver")
        print("  2. View All Drivers")
        print("  3. Search Driver")
        print("  4. Update Driver")
        print("  5. Remove Driver")
        print("  6. Back to Admin Menu")
        print("=" * 45)
        choice = input("Enter choice : ").strip()
        if choice == "1":
            add_driver()
        elif choice == "2":
            view_drivers()
        elif choice == "3":
            search_driver()
        elif choice == "4":
            update_driver()
        elif choice == "5":
            remove_driver()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please enter 1-6.")