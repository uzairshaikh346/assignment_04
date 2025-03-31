def greet(Name : str):
    print("Welcome " + Name)

def main():
    Name = input("Enter your name : ")
    greet(Name)

if __name__ == '__main__':
    main()