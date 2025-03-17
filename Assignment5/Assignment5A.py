#Class: CSE 1321L
#Section: P52
#Term: Spring 2025
#Instructor: Roshni Satish
#Name: Amelia Ellingson
#Lab#: Assignment5A

def pairDifference():

    num = input("Enter a list of numbers: ")

    try:

        number_list = [int(x.strip()) for x in num.split(",")]

        if len(number_list) < 2:
            print("Not enough numbers to calculate differences.")
            return tuple()

        difference = []
        for i in range(number_list - 1):
            listdiff = abs(number_list[i] - number_list[i + 1])
            difference.append(listdiff)

        result = tuple(difference)
        print(f"The absolute differences between consecutive numbers: {result}")
        return result


    except ValueError:
        print("Invalid input. Please enter comma-separated numbers")


pairDifference()