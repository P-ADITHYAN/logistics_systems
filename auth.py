# ============================================
#   auth.py - Login & Authentication System
# ============================================

# This is the path to our roles database file
ROLES_FILE = "database/roles.txt"


def login():
    print("\n" + "=" * 45)
    print("       LOGISTICS & DELIVERY SYSTEM")
    print("=" * 45)
    print("              LOGIN PORTAL")
    print("=" * 45)

    # Give user 3 attempts to login
    attempts = 0

    while attempts < 3:

        print(f"\nAttempt {attempts + 1} of 3")
        username = input("Enter Username : ").strip()
        password = input("Enter Password : ").strip()

        # Call verify function to check credentials
        result = verify_credentials(username, password)

        if result is not None:
            role, user_id = result
            print(f"\n✅ Login Successful!")
            print(f"   Welcome, {username}!")
            print(f"   Role : {role}")
            print("=" * 45)
            return role, user_id

        else:
            attempts += 1
            remaining = 3 - attempts

            if remaining > 0:
                print(f"❌ Invalid username or password.")
                print(f"   {remaining} attempt(s) remaining.")
            else:
                print("\n❌ Too many failed attempts.")
                print("   System will now exit.")
                return None


def verify_credentials(username, password):
    # Open the roles.txt file and check each line
    try:
        with open(ROLES_FILE, "r") as file:
            for line in file:

                # Remove newline and split by |
                line = line.strip()

                # Skip empty lines
                if line == "":
                    continue

                # Split into parts
                parts = line.split("|")

                # parts[0] = username
                # parts[1] = password
                # parts[2] = role

                stored_username = parts[0]
                stored_password = parts[1]
                stored_role     = parts[2]

                # Check if entered credentials match
                if username == stored_username and password == stored_password:
                    # Return role and user_id (username acts as ID)
                    return stored_role, stored_username

        # If loop finishes with no match found
        return None

    except FileNotFoundError:
        print("❌ ERROR: roles.txt file not found!")
        print("   Make sure database/roles.txt exists.")
        return None


def logout(username):
    print("\n" + "=" * 45)
    print(f"   Logged out successfully.")
    print(f"   Goodbye, {username}!")
    print("=" * 45)
    