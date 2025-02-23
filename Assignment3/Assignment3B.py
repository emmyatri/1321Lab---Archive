#Class: CSE 1321L
#Section: P52
#Term: Spring 2025
#Instructor: Roshni Satish
#Name: Amelia Ellingson
#Lab#: Assignment3B

#display function name
print("[Character Frequencies]")
#user input
string = (input("Enter a string: "))

#remove spaces and account for case
string = string.lower()
string = string.replace(" ", "")

#reference string
original_string = string

#character count loop
while string:
    #first character
    current_char = string[0]

    #count occurences by comparing the length before and after replacement
    original_length = 0
    new_length = 0

    for char in string:
        original_length += 1

    post_string = string.replace(current_char, "")

    for char in post_string:
        new_length += 1

    freq = original_length - new_length

    if freq == 1:
        print(f"{current_char} appears {freq} time.")
    else:
        print(f"{current_char} appears {freq} times.")

    string = post_string





