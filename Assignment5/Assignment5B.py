#Class: CSE 1321L
#Section: P52
#Term: Spring 2025
#Instructor: Roshni Satish
#Name: Amelia Ellingson
#Lab#: Assignment5B

import random

def game_board (width, height):
    board = []
    numberOfUndiscoveredTreasures = 0

    first_row = []
    for i in range(width):
        rand_num = random.random()
        if rand_num >= 0.7:
            first_row.append("T")
            numberOfUndiscoveredTreasures += 1
        else:
            first_row.append("O")
    board.append(first_row)

    for i in range(height - 1):
        row = []
        for j in range(width):
            rand_num = random.random()
            if rand_num >= 0.7:
                row.append("T")
                numberOfUndiscoveredTreasures += 1
            else:
                row.append("O")
        board.append(row)

    return board, numberOfUndiscoveredTreasures

def print_board(board, show_treasure=False):
    for row in board:
        for cell in row:
            if not show_treasure and cell == "T":
                print('O', end="")
            else:
                print(cell, end="")
        print()

def main():
    width = int(input("Width: "))
    height = int(input("Height: "))
    board, treasures = game_board(width, height)

if __name__ == "__main__":
    main()
