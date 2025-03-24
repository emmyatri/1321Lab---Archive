#Class: CSE 1321L
#Section: P52
#Term: Spring 2025
#Instructor: Roshni Satish
#Name: Amelia Ellingson
#Lab#: Lab6B

import random

number = random.randint(1,100)

while True:
    print("Guess the number I am thinking!")
    guess = int(input("Enter any number between 1 and 100: "))

    if guess == number:
        print(f"Correct! I was thinking of {number}")
        break

    elif guess > number:
        print("Too high!")

    else:
        print("Too low!")