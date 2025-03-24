#Class: CSE 1321L
#Section: P52
#Term: Spring 2025
#Instructor: Roshni Satish
#Name: Amelia Ellingson
#Lab#: Lab5B

#user input
size = int(input("Please enter a value for the size: "))

#print box
def print_box(size):
    for i in range(size):
        for j in range(size):
            print("*", end="")
        print()

def print_right_triangle(size):
    for i in range(size):
        for j in range(i + 1):
            print("*", end="")
        print()

def print_left_triangle(size):
    for i in range(size):
        for j in range (size - i - 1):
            print(" ", end="")
        for j in range(i + 1):
            print("*", end="")
        print()

print(f"This is the requested {size}x{size} box:")
print_box(size)

print(f"This is the requested right-facing {size}x{size} right-triangle:")
print_right_triangle(size)

print(f"This is the requested left-facing {size}x{size} right-triangle:")
print_left_triangle(size)



