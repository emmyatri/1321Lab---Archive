#Class: CSE 1321L
#Section: P52
#Term: Spring 2025
#Instructor: Roshni Satish
#Name: Amelia Ellingson
#Lab#: Assignment1C

#Centimeters to feet and inches
print("[Centimeters to Feet and Inches Converter]")
centimeters = float(input("Enter the length in centimeters: "))
inches = centimeters / float(2.54)
feet = int(inches // float(12))
extra_inches = inches % 12
extra_inches2 = str(round(extra_inches, 2))
feetstr = str(feet)
print("\nThe length is " + feetstr + " feet, and " + extra_inches2 + " inches")