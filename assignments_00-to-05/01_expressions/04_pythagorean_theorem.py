import math


def main():
    ab = float(input("Enter the length of AB : "))
    ac = float(input("Enter the length of AC : "))

    bc : float = math.sqrt(ab ** 2 + ac ** 2)

    print("The Length of BC is " + str(bc))


if __name__ == '__main__':
    main()