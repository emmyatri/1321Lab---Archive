#Class: CSE 1321L
#Section: P52
#Term: Spring 2025
#Instructor: Roshni Satish
#Name: Amelia Ellingson
#Lab#:Assignment4C

import A4C_Functions
from Assignment4.A4C_Functions import Display_Main_Menu, Deposit, Withdraw, Check_balance


def main():
    print("Welcome to the ATM!")
    name = input("Please enter your name: ")

    while True:
        try:
            balance = round(float(input("Enter your initial balance: $")), 2)
            if balance > 0:
                break
            else:
                print("Must deposit more than zero dollars.")
        except ValueError:
            print("Invalid number. Please enter a valid number")

    new_balance = balance

    while True:

        choice = Display_Main_Menu()

        if choice == 1:
            balance = Deposit(balance)
        elif choice == 2:
            balance = Withdraw(balance)
        elif choice == 3:
            balance = Check_balance()
        elif choice == 4:
            print(f"\nThank you for using our ATM, {name}! \nFinal Balance: ${balance}")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

