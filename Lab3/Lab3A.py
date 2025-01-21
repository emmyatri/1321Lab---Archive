#Class: CSE 1321L
#Section: P52
#Term: Spring 2025
#Instructor: Roshni Satish
#Name: Amelia Ellingson
#Lab#: Lab3A

balance = float(input("Amount owed: $"))
apr = float(input("APR: "))
mpr = float((apr / 12))
mpr2 = str(round(mpr,3))
min_payment = str(round((mpr/100) * balance, 2))
print("Monthly percentage rate: " + mpr2)
print("Minimum payment: $" + min_payment)

