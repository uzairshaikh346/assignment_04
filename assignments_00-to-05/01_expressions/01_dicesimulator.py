import random

num = 6 

def roll_dies():
    dice1: int = random.randint(1, num)  
    dice2: int = random.randint(1, num) 

    total = dice1 + dice2
    print(f" Dice 1: {dice1},  Dice 2: {dice2} → Total: {total}")

def main():
    for i in range(3):  
        print(f"Roll {i + 1}:")
        roll_dies()
        print()  

if __name__ == '__main__':
    main()
