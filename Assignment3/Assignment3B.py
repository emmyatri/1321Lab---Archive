#Class: CSE 1321L
#Section: P52
#Term: Spring 2025
#Instructor: Roshni Satish
#Name: Amelia Ellingson
#Lab#: Assignment3B

print("[Character Frequencies]")

#user input
word_input = str(input("Enter a string: "))
#user input set to lowercase w/ removed spaces
letter_count = word_input.lower().replace(" ", "")

original = letter_count

while letter_count:
    current_character = letter_count[0]

    original_length = 0
    new_length = 0

    for current_character in letter_count:
        original_length += 1

    text_after = letter_count


