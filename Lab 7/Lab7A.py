#Class: CSE 1321L
#Section: P52
#Term: Spring 2025
#Instructor: Roshni Satish
#Name: Amelia Ellingson
#Lab#: Lab7A

def isValid(width, height):
    return (width + height) > 30

def area(width, height):
    return width * height

def perimeter(width, height):
    return 2 * (width + height)

def main():
    while True:
        width = float(input("Enter width: "))
        height = float(input("Enter height: "))


        if isValid(width, height):
            print("This is a valid rectangle.")
            print(f"The area is: {area(width, height)}")
            print(f"The perimeter is: {perimeter(width, height)}")

        else:
            print("This is an invalid rectangle.")

        continue_rectangle = input("\nDo you want to enter another width and height? (Y/N): ").upper()
        if continue_rectangle != "Y":
            break
    print("\nProgram Ends.")

if __name__ == "__main__":
    main()