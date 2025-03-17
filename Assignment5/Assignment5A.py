#Class: CSE 1321L
#Section: P52
#Term: Spring 2025
#Instructor: Roshni Satish
#Name: Amelia Ellingson
#Lab#: Assignment5A

def pairDifference():

    num = input("Enter a list of numbers: ")

    number = [int(x.strip()) for x in num.split(",")]

    if len(number) < 2:
            print("Not enough numbers to calculate differences.")
            return tuple()

    difference = []
    for i in range (len(number) - 1):
            diff = abs(number[i] - number[i+1])
            difference.append(diff)

    result = tuple(difference)
    print(f"The absolute differences between consecutive numbers: {result}")
    return result


def main():
    pairDifference()

if __name__ == "__main__":
    main()