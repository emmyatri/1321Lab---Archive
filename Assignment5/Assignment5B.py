#Class: CSE 1321L
#Section: P52
#Term: Spring 2025
#Instructor: Roshni Satish
#Name: Amelia Ellingson
#Lab#: Assignment5B

import random

def treasure_game():
    width = int(input("Enter the width of the grid: "))
    height = int(input("Enter the height of the grid: "))

    board = []
    numberOfUndiscoveredTreasures = 0


    for i in range(height):
        row = []
        for j in range(width):
            if random.random() >= 0.7:
                row.append("T")
                numberOfUndiscoveredTreasures += 1
            else:
                row.append("O")
        board.append(row)

    initial_board = [['O' for _ in range(width)] for _ in range(height)]
    print(f"The number of undiscovered treasures is {numberOfUndiscoveredTreasures}")

    while numberOfUndiscoveredTreasures > 0:

        row = int(input(f"Enter the row number (0 to {height-1}): "))
        column = int(input(f"Enter the column number (0 to {width-1}): "))

        if row < 0 or row >= height or column <0 or column >= width:
            print("Invalid coordinates! Try again")
            continue

        if board[row][column] == "X":
            print("You've already found this treasure.")
            continue

        if board[row][column] == "T":
            print("Congratulations! You found a treasure!")
            initial_board[row][column] = 'X'
            numberOfUndiscoveredTreasures -= 1
            for row in initial_board:
                print(" ".join(row))

        else:
            print("No treasure here, try again!")
            initial_board[row][column] = 'O'

    if numberOfUndiscoveredTreasures == 0:
        print("Congratulations! You found all the treasure!")
        for row in initial_board:
            print(" ".join(row))


def main():
    treasure_game()

if __name__ == "__main__":
    main()






