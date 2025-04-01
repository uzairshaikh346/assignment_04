def double_it(num: int):
    while num < 100:
        double = num * 2
        print(str(num) + " double " + str(double))
        num = double

def main():
    num = int(input("ENter a number : "))
    double_it(num)

if __name__ == '__main__':
    main()