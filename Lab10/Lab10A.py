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

    #user input
    numOfLegs = int(input("How many legs does your chair have? "))

    #handling boolean
    rolling = input("Is your chair rolling (true/false): ").lower()
    rolling_chair = rolling == "true"

    material = input("What material is your chair made of? ")

    chair = Chair(numOfLegs, rolling_chair, material)

    print(f"Your chair has {chair.numOfLegs} legs, is {'' if chair.rolling == True  else "not" }rolling, and is made of {chair.material}.")
    print("This program is going to change that.")

    #second chair
    chair2 = (Chair(4, False, "wood"))
    print(f"Your chair has {chair2.numOfLegs} legs, is {'' if chair2.rolling else "not"} rolling, and is made of {chair2.material}.")



if __name__ == "__main__":
    main()
