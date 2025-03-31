max_number = 100

def main():

    user_input = int(input("Enter a number : "))
    while user_input < max_number:
        double_number = user_input * 2
        if double_number > max_number:
            break
        print(f"{user_input} doubled it {double_number}")

        user_input = double_number

if __name__ == '__main__':
    main()