#Class: CSE 1321L
#Section: P52
#Term: Spring 2025
#Instructor: Roshni Satish
#Name: Amelia Ellingson
#Lab#: Lab8A

email_list = []


def main():
    print("[Mailing List]")

    while True:
        print("\n1 - Add email"
              "\n2 - Delete email"
              "\n3 - List all emails"
              "\n4 - Quit")

        user_input = int(input("Make your selection: "))


        match user_input:

            case 1:
                print()
                email = input("Enter the email to be added: ")
                email_list.append(email)

            case 2:
                print()
                del_email = input("Enter the email to be deleted: ")
                if del_email in email_list:
                    email_list.remove(del_email)
                    print(f"{del_email} has been removed from the mailing list")
                else:
                    print(f"No such email in mailing list: {del_email}")
            case 3:
                print()
                print(email_list)
            case 4:
                print("Shutting down...")
                break
            case _:
                print("Invalid input. Enter a number (1-4)")





if __name__ == "__main__":
    main()