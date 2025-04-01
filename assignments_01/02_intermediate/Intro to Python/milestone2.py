#Planetary Weight Calculator

def weight_on_planets(weight:int):
    print("Select a planet to calculate your weight : ")
    print("1. Mercury")
    print("2. Venus")
    print("3. Mars")
    print("4. Jupiter")
    print("5. Saturn")
    print("6. Uranus")
    print("7. Neptune")

    choice = input("Enter the number of your choice: ")

    if choice == "1":
        x = weight * 0.376
        print(f"Your Mercury wait is {x}!")
    elif choice == "2":
        x = weight * 0.889
        print(f"Your Venus wait is {x}!")
    elif choice == "3":
        x = weight * 0.378
        print(f"Your Mars wait is {x}!")
    elif choice == "4":
        x = weight * 0.236
        print(f"Your Jupiter wait is {x}!")
    elif choice == "5":
        x = weight * 0.1081
        print(f"Your Saturn wait is {x}!")
    elif choice == "6":
        x = weight * 0.1081
        print(f"Your Uranus wait is {x}!")
    elif choice == "7":
        x = weight * 0.1140
        print(f"Your Naptune wait is {x}!")
    else:
        print("Invalid choice!")

def main():
    user_weight = int(input("Enter your body weight : "))
    y = weight_on_planets(user_weight)


if __name__ == '__main__':
    main()