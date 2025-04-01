import random
def main():

    round = 1
    score = 0
 

    while round <= 5:
        print(f"Round : {round}")
        user_number = random.randint(1,100)
        computer_number = random.randint(1,100)
        print(f"Your number is : {user_number}")
        user_guess = input("Do you think your number is higher or lower than the computer's?")
        user_guess = user_guess.lower()
        round += 1
        if user_guess == 'lower' and user_number < computer_number:
            print(f"You were right! The computer's number was {computer_number}")
            score += 1
            
        elif user_guess == 'higher' and user_number > computer_number:
            print(f"You were right! The computer's number was {computer_number}")
            score += 1
            
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_number}")
    if score <= 2:
        print(f"you lose your score = {score} is low!")
    else:
        print(f"you win your score = {score} is good!")


if __name__ == '__main__':
    main()