def main():
    Values = []

    get_input = input("Enter something to add in the list : ")

    while get_input != "":
       Values.append(get_input)
       get_input = input("Enter something to add in the list : ")

    print(Values)

if __name__ == '__main__':
    main()
