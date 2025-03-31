Inches_in_feet = 12

def main():
    feet: float = float(input("Enter Number of feet: "))  # Fixed typo
    inches = feet * Inches_in_feet
    print(f"This is {inches} inches")

if __name__ == '__main__':
    main()
