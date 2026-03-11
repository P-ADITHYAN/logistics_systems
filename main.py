

from auth import login
from menus.admin_menu import admin_menu
from menus.driver_menu import driver_menu
from menus.manager_menu import manager_menu


def main():
    while True:
        # Show login and get result
        result = login()

        # If login failed 3 times, exit program
        if result is None:
            break

        # Unpack role and user_id
        role, user_id = result

        # Route to correct menu based on role
        if role == "Admin":
            admin_menu(user_id)

        elif role == "Driver":
            driver_menu(user_id)

        elif role == "Manager":
            manager_menu(user_id)

        else:
            print("Unknown role detected. Contact admin.")


# Run the program
main()



