#Class: CSE 1321L
#Section: P52
#Term: Spring 2025
#Instructor: Roshni Satish
#Name: Amelia Ellingson
#Lab#: Lab10B

class Dog:
    def __init__(self, age, weight, name, furColor, breed):
        self.age = age
        self.weight = weight
        self.name = name
        self.furColor = furColor
        self.breed = breed


def bark():
    return "Woof! Woof!"


def eat(weight, food):
    Dog.weight = (weight + food)
    return Dog.weight

def rename(new_name):
    Dog.name = new_name


def main():

    print("You are about to create a dog.")

    #user input
    age = int(input("How old is the dog: "))
    weight = float(input("How much does the dog weigh: "))
    name = input("What is the dog's name: ")
    furColor = input("What color is the dog: ")
    breed = input("What breed is the dog: ")
    dog1 = Dog(age, weight, name, furColor, breed)

    #print input
    print(f"{dog1.name} is a {dog1.age} year old {dog1.furColor} {dog1.breed} that weighs {dog1.weight} lbs.")
    print(bark())

    #eat function
    food = float(input(f"{dog1.name} is hungry, how much should he eat: "))
    eat(weight, food)


    new_name = input(f"{dog1.name} isn't a very good name. What should they be renamed to: ")
    rename(new_name)

    print(f"{Dog.name} is a {dog1.age} year old {dog1.furColor} {dog1.breed} that weighs {Dog.weight} lbs.")



if __name__ == "__main__":
    main()