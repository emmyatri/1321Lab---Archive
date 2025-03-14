#Class: CSE 1321L
#Section: P52
#Term: Spring 2025
#Instructor: Roshni Satish
#Name: Amelia Ellingson
#Lab#:Assignment4C


def Display_Main_Menu():

    while True:
        print("ATM Main Menu:"
              "\n1. Deposit"
              "\n2. Withdraw"
              "\n3. Check Balance "
              "\n4. Exit")
        option_choice = int(input("Please choose an option (1-4): "))

        if 1 <= option_choice <= 4:
            return option_choice



def Deposit(balance):
        deposit = float(input("Enter the amount to deposit: $"))
        new_balance = (deposit + balance)
        print(f"Deposited: ${deposit} New balance: ${new_balance}")
        print()
        return new_balance

def Withdraw(balance):
    withdrawal = float(input("Enter the amount to withdraw: $"))
    if balance - withdrawal >= 0:
        new_balance2 = balance - withdrawal
        print(f"Withdrew ${withdrawal}. New balance: S{new_balance2}")
        return new_balance2
    else:
        print("Insufficient balance")
        return balance


def Check_balance(balance):
    print(f"Your current balance is: ${balance}")
    return balance