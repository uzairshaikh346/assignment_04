def add_many_numbers(numbers)-> int:
    
    total = 0
    for number in numbers:
        total += number


    return total

def main():
    list = [1,2,3,4,5]
    sum = add_many_numbers(list)
    print(sum)

if __name__ =='__main__':
    main()