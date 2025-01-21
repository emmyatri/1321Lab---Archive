#Class: CSE 1321L
#Section: P52
#Term: Spring 2025
#Instructor: Roshni Satish
#Name: Amelia Ellingson
#Lab#: Lab3B

#user input for class hours and grades received
course1 = int(input("Course 1 hours: "))
grade1 = int(input("Grade for course 1: "))
course2 = int(input("Course 2 hours: "))
grade2 = int(input("Grade for course 2: "))
course3 = int(input("Course 3 hours: "))
grade3 = int(input("Grade for course 3: "))
course4 = int(input("Course 4 hours: "))
grade4 = int(input("Grade for course 4: "))

#total hours & total quality points
total_hours = int(course1 + course2 + course3 + course4)
total_quality = int((grade1*course1) + (grade2*course2) + (grade3*course3) + (grade4*course4))
gpa = (float(total_quality / total_hours))

#gpa rounded to 2 decimal places
print("Total hours: ", total_hours)
print("Total quality points: ", total_quality)
print("Your GPA for this semester is ", round(gpa,2))

