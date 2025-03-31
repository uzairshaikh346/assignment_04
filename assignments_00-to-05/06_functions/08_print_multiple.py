def get(message : str , repeat : str):
    for i in range(repeat):
        print(message)



def main():
    message = input("Enter a message to print.")
    repeat = int(input("Enter a number to repeat the message."))

    get(message,repeat)

if __name__ == '__main__':
    main()