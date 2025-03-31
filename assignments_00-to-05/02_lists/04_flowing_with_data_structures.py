def add_three_copies(my_list, message):
    for i in range(3):
        my_list.append(message)



def main():
    messsage = input("Enter your message : ")
    my_list = []
    add_three_copies(my_list,messsage)
    print("List after:", my_list)


if __name__ == '__main__':
    main()