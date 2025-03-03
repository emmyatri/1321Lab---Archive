#Class: CSE 1321L
#Section: P52
#Term: Spring 2025
#Instructor: Roshni Satish
#Name: Amelia Ellingson
#Lab#: Lab8B

friend_list = []


def main():
    print("[Friend List]")

    while True:
        print("\n1 - Add friend"
              "\n2 - List friends"
              "\n3 - Quit")

        user_input = int(input("Make your selection: "))

        match user_input:

            case 1:
                friend_name = input("\nEnter your friend's name: ")
                friend_age = int(input("Enter your friend's age: "))
                friend_list.append(f"Name: {friend_name}, Age: {friend_age}")
                print("Friend added")

            case 2:
                for x in friend_list:
                    print(f"{x}")
            case 3:
                print("Shutting down...")
                break


if __name__ == "__main__":
    main()