def print_one_digit(num):
    print("The ones digit is", num % 10)

def main():
    user_input = int(input("Enter a number : "))
    print_one_digit(user_input)

if __name__ == '__main__':
    main()