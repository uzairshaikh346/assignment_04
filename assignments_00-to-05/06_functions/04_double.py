def double(number : int):
    double = number * 2
    return double


def main():
    user_input = int(input("Enter a number : "))
    num_2_times = double(user_input)
    print("Double that is", num_2_times)

if __name__ == '__main__':
    main()