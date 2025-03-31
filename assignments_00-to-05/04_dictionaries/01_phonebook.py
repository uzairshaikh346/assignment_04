def read_phone_book():
    phonebook = {}

    while True:
        name = input("enter a name : ")
        if name == "":
            break
        number = int(input("enter a phone number : "))
        phonebook[name] = number


    return phonebook

def print_phonebook(phonebook):

    for name in phonebook:
        print(f"{name} -> {phonebook[name]}")


def lookup_number(phonebook):

    while True:
        name = input("enter a name to lookup : ")
        if name == "":
            break
        if name not in phonebook:
            print(name + " is not in the phonebook")
        else:
            print(phonebook[name])


def main():
    phonebook = read_phone_book()
    print_phonebook(phonebook)
    lookup_number(phonebook)



if __name__ == '__main__':
    main()
