#Class: CSE 1321L
#Section: P52
#Term: Spring 2025
#Instructor: Roshni Satish
#Name: Amelia Ellingson
#Lab#: Assignment2A

#discount menu
print("[Discount Calculator]")
total_purchase = int(input("Enter your total purchase amount: $"))
member_status = input("Are you a member of the shopping club (Yes or No)? ").lower()

if total_purchase < 50:
    discount = 0
    print("Your discount is: " + str(discount))
elif 50 <= total_purchase <= 200:
    if member_status.startswith('y'):
        discount = total_purchase * .10
    else:
        discount = round(float(total_purchase * .5),2)
    print("Your discount is: " + str(discount))
elif total_purchase >= 200:
    if member_status.startswith('y'):
        discount = total_purchase*.15
    else:
        discount = round(float(total_purchase*.10),2)
    print("Your discount is: " + str(discount))


final_total = str(total_purchase - discount)
print("Your total price after discount is: $" + final_total)


