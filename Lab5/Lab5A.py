#Class: CSE 1321L
#Section: P52
#Term: Spring 2025
#Instructor: Roshni Satish
#Name: Amelia Ellingson
#Lab#: Lab5A


#welcome message

print("Please enter 10 numbers and this program will display the largest.")

largest_number = 0

for i in range (1,11):
    user_number = int(input(f"Please enter number {i}: "))

    if user_number > largest_number:
        largest_number = (user_number)

print("The largest number was " + str(largest_number) )