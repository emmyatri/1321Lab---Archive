#Class: CSE 1321L
#Section: P52
#Term: Spring 2025
#Instructor: Roshni Satish
#Name: Amelia Ellingson
#Lab#:Assignment4A

def format_word(word):
    if not word:
        return ""
    return word[0].upper() + word[1:].lower()

def convert_to_pascal_case(text):
    result = ""
    current_word = ""

    for char in text:
        if char == ' ':
            if current_word:
                result += format_word(current_word)
                current_word = ""
        else:
            current_word += char

    if current_word:
        result += format_word(current_word)
    return result


def main():
        user_input = input("Enter a string: ")
        pascal_case = convert_to_pascal_case(user_input)
        print(f"Pascal Case: {pascal_case}")

if __name__ == "__main__":
    main()