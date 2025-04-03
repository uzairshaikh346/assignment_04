# Guess number game computer
import random
def guess(number : int):
    computer = random.randint(1,number)
    guess = 0
    while guess != computer:
        guess = int(input(f"Guess a number between 1 and {number} : "))
        if guess > computer:
            print("Sorry, guess again. Too high.")
        elif guess < computer:
            print("Sorry, guess again. Too Low.")
    print("congrats, You guess the right number!")


def main():
    guess(10)

if __name__ == '__main__':
    main()
