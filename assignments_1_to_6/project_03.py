# number guess game user
import random
def computer_guess(number : int):
    low = 1
    high = number
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low
        feedback = input(f"Is {guess} too High (H), too Low(L) or correct(C)?").lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1

    print(f"Yayy, the computer guess your number , {guess} , correctly!!")


def main():
    computer_guess(10)

if __name__ == '__main__':
    main()

        