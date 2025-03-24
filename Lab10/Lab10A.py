#Class: CSE 1321L
#Section: P52
#Term: Spring 2025
#Instructor: Roshni Satish
#Name: Amelia Ellingson
#Lab#: Lab10A


class Chair:
    def __init__(self, numOfLegs = 4, rolling = False, material = "plastic"):
        self.numOfLegs = numOfLegs
        self.rolling = rolling
        self.material = material


def main():
    print("You are about to create a chair.")

    numOfLegs = int(input("How many legs does your chair have: "))

    rolling = input("Is your chair rolling (true/false): ").lower()
    if rolling == "true":
        rolling = ""
    else:
        rolling = "not "


    material = input("What is your chair made of: ")

    chair = Chair(numOfLegs, rolling, material)

    print(f"Your chair has {chair.numOfLegs} legs, is {chair.rolling}rolling, and is made of {chair.material}.")

    default_chair = Chair(4, False, "wood")
    default_chair.rolling = "not"



    print("This program is going to change that.")
    print(f"Your chair has {default_chair.numOfLegs} legs, is {default_chair.rolling} rolling, and is made of {default_chair.material}.")




if __name__ == "__main__":
    main()