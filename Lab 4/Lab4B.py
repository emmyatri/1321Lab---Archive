#Class: CSE 1321L
#Section: P52
#Term: Spring 2025
#Instructor: Roshni Satish
#Name: Amelia Ellingson
#Lab#: Lab4B

#welcome message + input
print("Welcome!")
user_number = float(input("Please input a number: "))
user_number2 = str(user_number)

#display numbers menu
print("What would you like to do with this number:")
print("0) Get the additive inverse of the number")
print("1) Get the reciprocal of the number")
print("2) Square the number")
print("3) Cube the number")
print("4) Exit the program")

operation = int(input())

match operation:

    case 0:
    # additive inverse
        result = str(user_number * -1)
        print(f"The additive inverse of "+ user_number2 + " is " + result)
    case 1:
        #reciprocal (1/n)
        if user_number == 0:
            print("Cannot divide by 0!")
        else:
            result = str(round (1 / user_number,3))
            print(f"The reciprocal of " + user_number2 + " is " + result)
    case 2:
        # square the number
            result = str(round(user_number ** 2, 2))
            print(f"The square of " + user_number2 + " is " + result)
    case 3:
        # cube the number
        result = str(round(user_number ** 3, 2))
        print(f"The cube of " + user_number2 + " is " + result)
    case 4:
        print("Thank you, goodbye!")
    case _:
        print("Invalid option!")
