#Class: CSE 1321L
#Section: P52
#Term: Spring 2025
#Instructor: Roshni Satish
#Name: Amelia Ellingson
#Lab#: Assignment3C

print("Welcome to the Guess the Word game!")
word = input("Enter a word to guess (lowercase letters only): ").lower()
hidden_word = "_" * len(word)

print("The word to guess is: ", hidden_word)

while "_" in hidden_word:
    guess = input("Guess a letter: ").lower()

    if guess in word:
        new_hidden_word = ""
        for i in range(len(word)):
            if word[i] == guess:
                new_hidden_word += guess
            else:
                new_hidden_word += hidden_word[i]
        hidden_word = new_hidden_word

        if "_" in hidden_word:
            print("Good guess! \nThe word to guess is: ", hidden_word)
        else:
            print("Good guess! \nCongratulations! You've guessed the word:", word)
    else:
        print("Oops! That letter is not in the word.")




