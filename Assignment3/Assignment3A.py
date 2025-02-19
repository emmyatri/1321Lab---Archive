#Class: CSE 1321L
#Section: P52
#Term: Spring 2025
#Instructor: Roshni Satish
#Name: Amelia Ellingson
#Lab#: Assignment3A


odd_num = int(input("Enter an odd number for the size of the diamond: "))

if odd_num % 2 == 0:
    print(f"Size must be an odd number; we will increase it to {odd_num + 1}")
    odd_num += 1

number = 0

for i in range(odd_num//2 + 1):

    for j in range(odd_num//2 - i):
        print(" ", end="")

    for j in range(2*i + 1):
        print(number, end="")
        number = (number + 1) % 10

    print()

for i in range(odd_num//2 - 1, -1, -1):
    for j in range(odd_num//2 - i):
        print(" ", end="")

    for j in range(2*i + 1):
        print(number, end="")
        number = (number + 1) % 10

    print()



