# password generator

import random

def main():
    chars= "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+-=}[{]|\\:;\"'<>,.?/~`";


    number = int(input("Enter the number of password you want to generate? : "))

    Length = int(input("Enter the Length of password you want to generate? : "))

    for pwd in range(number):
        Password = ''
        for x in range(Length):
            Password += random.choice(chars)
        print(Password)

if __name__ == '__main__':
    main()