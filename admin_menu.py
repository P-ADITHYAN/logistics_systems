# ============================================
#   admin_menu.py
# ============================================

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modules.order_management   import order_management_menu
from modules.driver_management  import driver_management_menu
from modules.vehicle_management import vehicle_management_menu
from modules.route_assignment   import route_assignment_menu
from modules.fuel_tracking      import fuel_tracking_menu
from modules.reports            import reports_menu


def admin_menu(user_id):
    while True:
        print("\n" + "=" * 45)
        print("         ADMIN CONTROL PANEL")
        print(f"         Logged in as : {user_id}")
        print("=" * 45)
        print("  1. Order Management")
        print("  2. Driver Management")
        print("  3. Vehicle Management")
        print("  4. Route Assignment")
        print("  5. Fuel Tracking")
        print("  6. Reports")
        print("  7. Logout")
        print("=" * 45)
        choice = input("Enter choice : ").strip()
        if choice == "1":
            order_management_menu()
        elif choice == "2":
            driver_management_menu()
        elif choice == "3":
            vehicle_management_menu()
        elif choice == "4":
            route_assignment_menu()
        elif choice == "5":
            fuel_tracking_menu()
        elif choice == "6":
            reports_menu()
        elif choice == "7":
            print(f"\nLogged out. Goodbye {user_id}!")
            break
        else:
            print("Invalid choice. Please enter 1-7.")