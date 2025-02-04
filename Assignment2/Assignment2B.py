#Class: CSE 1321L
#Section: P52
#Term: Spring 2025
#Instructor: Roshni Satish
#Name: Amelia Ellingson
#Lab#: Assignment2B

#welcome menu
print("[Loan Approval System]")

age = int(input("Enter your age: "))
income = int(input("Enter your income: "))
creditscore = int(input("Enter your credit score: "))

if age < 18:
    print("You do not qualify for a loan due to age.")

