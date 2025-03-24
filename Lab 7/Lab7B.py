#Class: CSE 1321L
#Section: P52
#Term: Spring 2025
#Instructor: Roshni Satish
#Name: Amelia Ellingson
#Lab#: Lab7B

from MyMath import my_max, my_min, my_avg

def main():
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))

    minimum = my_min(num1, num2)
    maximum = my_max(num1, num2)
    average = my_avg(num1, num2)

    print(f"Min is {minimum}")
    print(f"Max is {maximum}")
    print(f"Average is {average}")

if __name__ == "__main__":
    main()
