max_length = 5

def shorten(lst):
    if lst > max_length:
        lst_elem = lst.pop()
        print(lst_elem)

def get_elem():


    lst = []

    elem = input("Please enter an element of the list or press enter to stop. ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop. ")

    return lst


