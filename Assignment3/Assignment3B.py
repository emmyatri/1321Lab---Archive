#Class: CSE 1321L
#Section: P52
#Term: Spring 2025
#Instructor: Roshni Satish
#Name: Amelia Ellingson
#Lab#: Assignment3B

#display function name
print("[Character Frequencies]")
#user input
word_input = (input("Enter a string: "))

#user input set to lowercase w/ removed spaces
letter_count = word_input.lower()
letter_count = (word_input.replace(" ", ""))

word_input = letter_count

while letter_count:
    #Get first character
    current_character = letter_count[0]

    #count occurrences
    original_length = 0
    new_length = 0

    for current_character in letter_count:
        original_length += 1

    text_after = letter_count.replace((current_character), "")

    for current_character in text_after:
        new_length += 1

    frequency = original_length - new_length

    if frequency == 1:
        print(f"The letter {current_character} appears {frequency} time.")
    else:
        print(f"The letter {current_character} appears {frequency} times.")
    break

    text = text_after




