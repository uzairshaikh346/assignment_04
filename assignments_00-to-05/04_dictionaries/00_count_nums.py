numbers_count = {} 

while True:
    user_input = input("Enter a number (or press Enter to stop): ")
    if user_input == "":  
        break

    num = int(user_input) 
    numbers_count[num] = numbers_count.get(num, 0) + 1 



for num, count in numbers_count.items():
    print(f"{num} appears {count} times.")
