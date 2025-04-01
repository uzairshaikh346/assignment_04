#Planetary Weight Calculator


def mars_weight(weight:int):
    w_on_mars = weight * 0.378
    rounded = round(w_on_mars , 2)
    return rounded

def main():
    user_weight = int(input("Enter your body weight : "))
    x = mars_weight(user_weight)
    print(f"Your weight on mars is : {x}")


if __name__ == '__main__':
    main()