# Rock paper scissor game
import random

def play():

    computer = random.choice(['r','p','s'])
    user = input("what your choice? 'r' for Rock , 'p' for Paper and 's' for Scissor ")

    if user == computer:
        return "It's a Tie !'"

    if is_win(user,computer):
        return "You won!"

    return 'You Lost!'







def is_win(player, opponent):

    if (player == 'r' and opponent == 'p') or (player == 'p' and opponent == 's') or (player == 's' and opponent == 'r'):
        return True
    

def main():

    print(play())

if __name__ == '__main__':
    main()