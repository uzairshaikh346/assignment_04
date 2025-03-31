Adult_age = 18

def is_adult(age):
    if age >= Adult_age:
        return True
    return False

def main():
    age = int(input("Enter your age : "))
    print(is_adult(age))

if __name__ == '__main__':
    main()