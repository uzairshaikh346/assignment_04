def is_odd(number : int):

    remainder = number % 2
    return remainder

def main():

    for i in range(10):
        if is_odd(i):
            print("Odd")
        else:
            print("Even")

if __name__ == '__main__':
    main()
