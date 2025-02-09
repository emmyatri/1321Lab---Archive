#Class: CSE 1321L
#Section: P52
#Term: Spring 2025
#Instructor: Roshni Satish
#Name: Amelia Ellingson
#Lab#: Assignment2C


#welcome message
print("Welcome to the RPG Game! \nChoose your class 1. Warrior 2. Mage 3. Healer")
character = int(input("Enter the number of your class (1/2/3): "))

if character < 1 or character > 3:
    print("Invalid class choice. The game ends.")
else:
    #Handle Valid Character
    match character:
        case 1:
            character = "Warrior"
            print("You have chosen Warrior! You are strong and brave. \nWhat would you like to do? 1. Attack with your sword 2. Defend with your shield.")
        case 2:
            character = "Mage"
            print("You have chosen Mage! You wield powerful magic. \nWhat would you like to do? 1. Cast fireball. 2. Cast a healing spell.")
        case 3:
            character = "Healer"
            print("You have chosen Healer! You are kind and supportive. \nWhat would you like to do? 1. Heal your ally. 2. Attack with your staff.")


    action = int(input("Choose your action (1/2) "))

match character:
    case "Warrior":
        match action:
            case 1:
                print("You swing your sword and defeat the enemy!")
            case 2:
                print("You raise your shield and block the enemy's attack!")
            case _:
                print("Invalid action choice.")
    case "Mage":
        match action:
            case 1:
                print("You cast a fireball and scorch the enemy!")
            case 2:
                print("You cast a healing spell and restore your energy.")
            case _:
                print("Invalid action choice.")
    case "Healer":
        match action:
            case 1:
                print("You heal your ally and boost their morale!")
            case 2:
                print("You swing your staff and knock out the enemy!")
            case _:
                print("Invalid action choice.")

print("Thank you for playing!")