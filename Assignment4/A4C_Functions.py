#Class: CSE 1321L
#Section: P52
#Term: Spring 2025
#Instructor: Roshni Satish
#Name: Amelia Ellingson
#Lab#:Assignment4C


def Display_Main_Menu():

    while True:
        print("\nATM Main Menu:"
              "\n1. Deposit"
              "\n2. Withdraw"
              "\n3. Check Balance "
              "\n4. Exit")
        option_choice = int(input("Please choose an option (1-4): "))

        if option_choice >= 1 or option_choice <= 4:
            return option_choice
        break



def Deposit(balance):
        deposit = int(input("Enter the amount to deposit: $"))
        new_balance = str(deposit + balance)
        print(new_balance)

def Withdraw(balance):
    withdrawal = int(input("Enter the amount to withdraw: $"))
    if withdrawal <= balance:
        new_balance2 = balance - withdrawal
        print(f"Withdrew ${withdrawal}. New balance: S{new_balance2}")
    else:
        print("Insufficient balance")


def Check_balance(balance):
    print(f"Your current balance is {balance}")