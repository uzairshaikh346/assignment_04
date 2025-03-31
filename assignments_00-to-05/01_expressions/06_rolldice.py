import random
num_inside = 6

def main():
   dice1 = random.randint(1,num_inside)
   dice2 = random.randint(1,num_inside)

   total = dice1 + dice2

   print("Dice have", num_inside, "sides each.")
   print("First dice:", dice1)
   print("Second dice:", dice2)
   print("Total of two dice:", total)

main()