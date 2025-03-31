import random

def main():

    secret_number = random.randint(1,99)

    print("I am thinking of a number between 0 and 99")

    guess = int(input("Guess a number : "))

    while secret_number != guess:
        if secret_number > guess:
            print("you guess too low.")
        else:
            print("you guess to high.")

        guess = int(input("Guess a number : "))

    print("Congrats! The number was: " + str(secret_number))

if __name__ == '__main__':
    main()
        