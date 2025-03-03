#Class: CSE 1321L
#Section: P52
#Term: Spring 2025
#Instructor: Roshni Satish
#Name: Amelia Ellingson
#Lab#:Assignment4B

#check length
def check_length(password):
    return len(password) >= 8

#case-sensitivity
def check_upper_lower(password):
    has_upper = False
    has_lower = False

    for char in password:
        if char.isupper():
            has_upper = True
        if char.islower():
            has_lower = True

    return has_upper and has_lower

#special character sensitivity
def check_special_character(password):

    has_spec_char = False

    if "@" in password or "!" in password or "#" in password:
        has_spec_char = True
    return has_spec_char
    
#main function
def main():
    while True:

        #user input
        password = (input("Enter a password: "))

        #run functions
        length_check = check_length(password)
        case_check = check_upper_lower(password)
        spec_char_check = check_special_character(password)


        #output for correctly entered password
        if length_check and case_check and spec_char_check:
            print("Password is strong!")
            break

        #error code messages
        print("Password doesn't meet requirements: ")
        if not length_check:
            print("Must be at least 8 characters long.")
        if not case_check:
            print("Must contain both uppercase and lowercase letters.")
        if not spec_char_check:
            print("Must include at least one special character (!, @, #).")



if __name__ == "__main__":
    main()