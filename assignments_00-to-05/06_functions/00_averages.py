def avg(a: float , b : float):

    sum = a + b
    avg = sum / 2
    return avg

def main():

    average1 = avg(5 , 10)
    average2 = avg(15 , 20)

    final_average = avg( average1 , average2 )

    print("avg_1", average1)
    print("avg_2", average2)
    print("final", final_average)


if __name__ == '__main__':
    main()