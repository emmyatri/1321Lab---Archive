#Class: CSE 1321L
#Section: P52
#Term: Spring 2025
#Instructor: Roshni Satish
#Name: Amelia Ellingson
#Lab#: Lab6A

def multiplication(a, b) -> int:
    result = 0
    for _ in range(b):
        result += (a)
    return result

def exponentiate(base, exponent) -> int:
    if exponent == 0:
        return 1
    result = 1
    for _ in range(exponent):
        result = 0
        for _ in range(exponent):
            result += base
        return result

def user_input() -> int:
    print("Multiplication and Exponent Calculator\nChoose option 1 for Multiplication"
          "\nChoose option 2 for Exponentiation\nChoose option 3 to Exit")
    return int(input())

while True:
    try:
        operation = user_input()

        match operation:
            case 1:
                a = int(input("Enter an operand: "))
                b = int(input("Enter another operand: "))
                result = multiplication(a,b)
                print(f"{a} x {b} = {result}")
                break

            case 2:
                base = int(input("Enter an operand: "))
                exponent = int(input("Enter another operand: "))
                result = exponentiate(base, exponent)
                print(f"{base}^{exponent} = {result}")
                break

            case 3:
                print("Closing the Calculator...")
                break

            case _:
                print("Invalid Choice")
                break


    except ValueError:
        print("Invalid Choice)")




