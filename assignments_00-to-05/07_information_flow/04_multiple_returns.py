def get_user_info():
    first_name = input("Enter your first name : ")
    last_name = input("Enter your last name : ")
    email = input("Enter your email : ")

    return first_name,last_name,email

def main():
    user_data = get_user_info()
    print("Recieved the following user data : " + user_data)

if __name__ == '__main__':
    main()