import random

def guess_number(num: int, number: int) -> bool:
    if num > number:
        print("Your number is too high.")
    elif num < number:
        print("Your number is too low.")
    else:
        print(f" Congrats! The number was: {number}")
        return True
    return False

def main():
    number = random.randint(1, 100)
    print("Guess my number between 1 and 100!")

    while True:
            user_number = int(input("Enter a number: "))
            if guess_number(user_number, number):
                break

if __name__ == '__main__':
    main()
