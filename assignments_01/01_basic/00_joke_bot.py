def print_joke(prompt):
    if prompt.lower() == 'joke':
        print("""Why don’t skeletons fight each other?
              Because they don’t have the guts! 😆""")
    else:
        print("Sorry I only tell jokes.")

def main():
    user_input = input("What do you want? ")

    print_joke(user_input)

if __name__ == '__main__':
    main()
