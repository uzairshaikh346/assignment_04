def main():
    num = 10
    for i in range(11):
        print(num , end=" ")
        num -= 1
        if num < 0:
            print("liftoff!")
if __name__ == '__main__':
    main()