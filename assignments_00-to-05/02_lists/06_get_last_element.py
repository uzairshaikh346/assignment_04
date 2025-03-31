def get_1st_element(element_list):
    if element_list:
        print("Last Element:", element_list[len(element_list) - 1])
    else:
        print("List is empty.")

def get_list():
    elements = []
    elem = input("Please enter an element of the list or press enter to stop: ")
    while elem != "":
        elements.append(elem)
        elem = input("Please enter an element of the list or press enter to stop: ")
    return elements

def main():
    get_element = get_list()
    get_1st_element(get_element)

if __name__ == '__main__':
    main()
