# ============================================
#   driver_menu.py
# ============================================

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modules.delivery_tracking import (
    view_my_orders,
    update_delivery_status,
    view_my_performance
)
from modules.fuel_tracking import add_fuel_record


def driver_menu(user_id):
    while True:
        print("\n" + "=" * 45)
        print("           DRIVER PORTAL")
        print(f"           Driver : {user_id}")
        print("=" * 45)
        print("  1. View My Assigned Orders")
        print("  2. Update Delivery Status")
        print("  3. Submit Fuel Record")
        print("  4. View My Performance")
        print("  5. Logout")
        print("=" * 45)
        choice = input("Enter choice : ").strip()
        if choice == "1":
            view_my_orders(user_id)
        elif choice == "2":
            update_delivery_status(user_id)
        elif choice == "3":
            add_fuel_record()
        elif choice == "4":
            view_my_performance(user_id)
        elif choice == "5":
            print(f"\nLogged out. Goodbye {user_id}!")
            break
        else:
            print("Invalid choice. Please enter 1-5.")