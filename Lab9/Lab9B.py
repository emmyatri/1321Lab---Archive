#Class: CSE 1321L
#Section: P52
#Term: Spring 2025
#Instructor: Roshni Satish
#Name: Amelia Ellingson
#Lab#: Lab9B


def register(users):
    print("\n[Register]")
    username = input("Username: ")
    password = input("Password: ")
    users[username] = password
    print("User successfully added!")

def change_password(users, username):
    new_password = input("Password: ")
    users[username] = new_password
    print("Password updated successfully!")

def main():
    users = {}

    while True:
        print("\nChoose an option \n1 - Login \n2 - Registration \nE - Exit")
        choice = input()

        if choice == "1":
            print()
            print("[Login]")
            username = input("Username: ")
            password = input("Password: ")

            if username in users and users[username] == password:
                print("Success!")

                while True:
                    print("\nChoose an option \n3 - Change Password \n4 - Logout \nE - Exit")
                    login_choice = input()

                    if login_choice == '3':
                        change_password(users, username)

                    elif login_choice == '4':
                        print("\nLogging out...")
                        break
                    elif login_choice == 'E':
                        print("\nTerminating...")
                        break
                    else:
                        print("Invalid choice.")
            else:
                print("Incorrect username/password!")

        elif choice == '2':
            register(users)

        elif choice == 'E':
            print("Terminating...")
            break
        else:
            print("Invalid choice.")



if __name__ == "__main__":
    main()