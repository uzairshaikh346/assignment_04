def in_range(n,low,high):
    if n >= low and n <= high:
        return True
    
    return False

def main():
    n = int(input("Enter a Number"))
    low = int(input("Enter low number"))
    high = int(input("Enter high Number"))

    result  = in_range(n,low,high)
    print(result)

if __name__ == "__main__":
    main()