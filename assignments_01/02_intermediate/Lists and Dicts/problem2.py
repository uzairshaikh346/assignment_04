# problem2


lst = ['mango' , 'hammad' , 4 ,'pakstan' , 2.5 ,]
def accec_element(lst  , index):

    if index < len(lst):
        print(lst[index])
    else:
        print("index does not exist!")



def modifying_element(lst , index , value):

    if index < len(lst):
        lst[index] = value
        print(lst)
    else:
        print("index does not exist!")


def slicing_list(lst, start : int, end : int):
    if 0 <= start < len(lst) and 0 < end <= len(lst) and start < end:
        print(lst[start:end])
    else:
        print("index does not exist!")


def main():

    print(lst)
    print("1 .Accessing Elements ")
    print("2 .Modifying Elements ")
    print("3 .Slicing the List ")
    user_input = int(input("select an operation : "))

    if user_input == 1:
        index_element = int(input("Enter an index to acces the element ."))
        accec_element(lst, index_element)
    elif user_input == 2:
        index_element = int(input("Enter an index to modify the element ."))
        value = (input("Enter a new value to add ."))
        modifying_element(lst,index_element,value)
    elif user_input == 3:
        start = int(input("Enter a start index ."))
        end = int((input("Enter a end index .")))
        slicing_list(lst , start , end)
    else:
        print("select a correct operation!")
        




if __name__ == '__main__':
    main()
