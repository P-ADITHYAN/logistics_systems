# ============================================
#   manager_menu.py
# ============================================

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modules.route_assignment import (
    assign_route,
    view_active_routes,
    view_all_routes
)
from modules.reports import (
    driver_performance_report,
    vehicle_performance_report,
    operational_summary
)
from modules.order_management import view_orders


def manager_menu(user_id):
    while True:
        print("\n" + "=" * 45)
        print("         MANAGER PORTAL")
        print(f"         Manager : {user_id}")
        print("=" * 45)
        print("  1. Assign Route")
        print("  2. View Active Routes")
        print("  3. View All Routes")
        print("  4. Monitor All Orders")
        print("  5. Driver Performance Report")
        print("  6. Vehicle Performance Report")
        print("  7. Operational Summary")
        print("  8. Logout")
        print("=" * 45)
        choice = input("Enter choice : ").strip()
        if choice == "1":
            assign_route()
        elif choice == "2":
            view_active_routes()
        elif choice == "3":
            view_all_routes()
        elif choice == "4":
            view_orders()
        elif choice == "5":
            driver_performance_report()
        elif choice == "6":
            vehicle_performance_report()
        elif choice == "7":
            operational_summary()
        elif choice == "8":
            print(f"\nLogged out. Goodbye {user_id}!")
            break
        else:
            print("Invalid choice. Please enter 1-8.")