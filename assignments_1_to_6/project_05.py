# hangman word guessing game
import random

def choose_word():
    words = ["Apple", "Mango", "Banana", "Orange", "Cherry"]
    return random.choice(words).lower()

def display(word, guessed_letters):
    return " ".join([letter.upper() if letter in guessed_letters else "_" for letter in word])

def hangman():
    word = choose_word()  
    guessed_letters = set(word[0])  
    attempts = 6  

    print("\nWelcome to Hangman!")
    print(f"The first letter is: {word[0].upper()}")  
    print("Guess the word letter by letter. You have 6 chances.\n")

    while attempts > 0:
        print("\nWord:", display(word, guessed_letters))  
        guess = input("Enter a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed this letter. Try a different one!")
            continue

        guessed_letters.add(guess)  

        if guess in word:
            print("Nice! That letter is in the word.")
            if set(word) <= guessed_letters:
                print(f"\nCongratulations! You guessed the word: {word.upper()}")
                return
        else:
            attempts -= 1
            print(f"Incorrect guess. {attempts} attempts left.")

        if attempts == 0:
            print(f"\nGame Over! The word was: {word.upper()}")

hangman()
