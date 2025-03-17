#Class: CSE 1321L
#Section: P52
#Term: Spring 2025
#Instructor: Roshni Satish
#Name: Amelia Ellingson
#Lab#: Lab9B


registration_log = {}

def login_screen(username, password):

    user_input = int(input())

    match user_input:

        case 1:
            print("[Login]")
            username = input("Username: ")
            password = input("Password: ")
            if not username or password in registration_log:
                print("Incorrect username/password")
            else:
                user_account(username, password)

        case 2:
            print("[Register]")
            username = input("Username: ")
            password = input("Password: ")
            registration_log["Username"] = username
            registration_log["Password"] = password
            print("User Successfully Added")
            print(registration_log)

def user_account(username, password):
    print("\nChoose an option \n3 - Change Password \n4 - Logout \nE - Exit ")
    choice = input()

    match choice:

        case 3:
            print("[Changing password]")
            new_password = input("Password: ")
            registration_log.update({"password" : new_password})


def main():
    while True:
        print("\nChoose an option \n1 - Login \n2 - Register \nE - Exit ")
        user_input = int(input())
        login_screen(username, password)







if __name__ == "__main__":
    main()