#Class: CSE 1321L
#Section: P52
#Term: Spring 2025
#Instructor: Roshni Satish
#Name: Amelia Ellingson
#Lab#: Lab3C

#sandwich number input
small_sand = int(input("Enter the number of small sandwiches: "))
medium_sand = int(input("Enter the number of medium sandwiches: "))
large_sand = int(input("Enter the number of large sandwiches: "))
xtlarge_sand = int(input("Enter the number of extra-large sandwiches: "))

print("You've entered", small_sand, "small sandwiches.", "You've entered", medium_sand, "medium sandwiches.",
"You've entered", large_sand, "large sandwiches.", "You've entered", xtlarge_sand, "extra-large sandwiches.")

small_cooktime = int(30*small_sand)
medium_cooktime = int(60*medium_sand)
large_cooktime = int(75*large_sand)
xtlarge_cooktime = int(135*xtlarge_sand)

total_second = (int(small_cooktime + medium_cooktime + large_cooktime + xtlarge_cooktime))
minutes = str(total_second // 60)
seconds = str(total_second % 60)
print("Total cooking time is " + minutes + " minutes and " + seconds + " seconds.")
