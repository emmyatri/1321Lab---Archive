#Class: CSE 1321L
#Section: P52
#Term: Spring 2025
#Instructor: Roshni Satish
#Name: Amelia Ellingson
#Lab#: Lab4A

#grade input

grade = float(input("Enter your grade: "))

#grade parameters
if grade > 97 and grade <= 100:
    print("Letter grade is: A+")
if grade >= 94 and grade <= 97:
    print("Letter grade is: A")
if grade >= 91 and grade < 94:
    print("Letter grade is: A-")
if grade >= 88 and grade < 91:
    print("Letter grade is: B+")
if grade >= 85 and grade < 88:
    print("Letter grade is: B")
if grade >= 82 and grade < 85:
    print("Letter grade is: B-")
if grade >= 79 and grade < 82:
    print("Letter grade is: C+")
if grade >= 76 and grade < 79:
    print("Letter grade is: C")
if grade >= 73 and grade < 76:
    print("Letter grade is: C-")
if grade >= 70 and grade < 73:
    print("Letter grade is: D+")
if grade >= 67 and grade < 70:
    print("Letter grade is: D")
if grade >= 64 and grade < 67:
    print("Letter grade is: D-")
if grade >= 0 and grade < 64:
    print("Letter grade is: F")