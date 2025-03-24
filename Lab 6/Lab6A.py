#Class: CSE 1321L
#Section: P52
#Term: Spring 2025
#Instructor: Roshni Satish
#Name: Amelia Ellingson
#Lab#:Lab6A

def main():
    running = True
    while running:
        print("Multiplication and Exponent Calculator")
        print("Choose option 1 for Multiplication")
        print("Choose option 2 for Exponentiation")
        print("Choose option 3 to Exit")

        choice = int(input())

        match choice:

            case 1:
                operand1 = int(input("\nEnter an operand: "))
                operand2 = int(input("Enter the other operand: "))
                result = 0
                for _ in range(operand2):
                    result += operand1
                print(f"{operand1} x {operand2} = {result}\n")

            case 2:
                base = int(input("\nEnter the base: "))
                exponent = int(input("Enter the exponent: "))
                result = 1
                for _ in range(exponent):
                    result1 = 0
                    for _ in range(base):
                        result1 += result
                    result = result1
                print(f"{base}^({exponent}) = {result}\n")

            case 3:
                print("\nClosing the calculator...")
                break

            case _:
                print("\nInvalid Choice\n")

if __name__ == "__main__":
    main()