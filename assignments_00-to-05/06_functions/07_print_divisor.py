def print_divisor(number : int):
    print("Here are the divisors of", number)
    for i in range(number):
        current_divisor = i + 1
        if number % current_divisor == 0:
            print(current_divisor)


def main():
    user_input = int(input("Enter a number : "))
    print_divisor(user_input)

if __name__ == '__main__':
    main()