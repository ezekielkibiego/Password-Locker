#!/usr/bin/env python3.8
from user import User
from details import Details

def function():
	print("               ____                             _             ")
	print("              |  _ \                           | |            ")
	print("              | |_) )  ____    ___    ___      | |            ")
	print("              |  __/  / _  \  / __|  / __|     | |            ")
	print("              | |    / (_|  \ \  \__  \ \__    | |___         ")
	print("              |_|    \_____ / /___ /   /___/   |_____)        ")
function()

def create_new_user(username, password):
    '''
    create a new user
    '''
    new_user = User(username, password)
    return new_user
def save_user(user):
    '''
    save user
    '''
    user.save_user()
def delete_user(username):
    '''
    delete user
    '''
    User.delete_user(username)
def find_user_existing(username):
    '''
    find if user exists
    '''
    return User.user_exist(username)
def find_user_password(username, password):
    '''
    find if the user enter the correct username and password
    '''
    return User.check_user(username, password)
def create_new_detail(account_name, account_username, account_password):
    '''
    create a new detail
    '''
    new_detail = Details(
        account_name, account_username, account_password)
    return new_detail
def save_details(details):
    '''
    save details
    '''
    details.save_details()
def display_details():
    """
    display details
    """
    return Details.display_details()
def delete_detail(account_media):
    '''
    delete details
    '''
    return Details.delete_details(account_media)
def find_details(account_name):
    '''
    find details
    '''
    return Details.find_by_account_media(account_name)
def generate_password(password_length):
    """
    generate a random password
    """
    return Details.generate_password(password_length)

def main():
    print("Hi, Please enter your ?")
    name = input()
    while True:
        print('.......................................................................................')
        print(f"Welcome {name} ...\n kindly, use the following to proceed.\n ca ...  Create a New Account \n fa ...  Find Existing Account  \n lg ... SignIn to your account  \n da ... display account \n ex ... exit from app")
        print('.......................................................................................')
        short_code=input("").lower().strip()

        if short_code == 'ca':
            print("Create a New User Account")
            print('.......................................................................................')
            print("Enter your username .....")
            username = input()
            print("Enter your password .....")
            user_password = input()
            save_user(create_new_user(
                      username, user_password))
            print('.......................................................................................')
            print(
                f"Bravo {name}! You've created Account successfully. lg to SignIn to your account")
            print('.......................................................................................')

        elif short_code == 'lg' or short_code == 'da':
            print('.......................................................................................')
            print("Enter your username ...")
            username = input()
            print("Enter your password ...")
            user_password = input()
        
            if find_user_existing(username):
                if find_user_password(username, user_password):
                    print("\n")
                    print(f"Happy to see you again, welcome {username}")
                    print('.......................................................................................')
                    while True:
                        print("Select one of the following short codes to proceed: \n")
                        print(
                            "1. Create a new details account\n2. View saved details account\n3. Delete details account\n4. Sign Out")
                        print("\n")
                        log_choice = int(input())
                        if log_choice == 1:
                            print(
                                "Enter the account name you want to create example, FB, Twitter, Pinterest...")
                            account_name = input()
                            print("Enter the username of the account you have created")
                            account_username = input()
                            print('\n')
                            print('.......................................................................................')
                            print(
                                "Do you want to generate a random password or enter own password?\n \n   Enter 1 to generate a random password\n   Enter 2 to enter your own password")
                            print('.......................................................................................')
                            print("\n")
                            choice = int(input())
                            if choice == 1:
                                print(
                                    "Enter legnth of your desired password?")
                                password_length = int(input())
                                account_password = generate_password(
                                    password_length)
                                print(
                                    f"Your generated password is {account_password}")
                            elif choice == 2:
                                print("Enter own password of the account")
                                account_password = input()
                            else:
                                print("Invalid input")
                            save_details(create_new_detail(
                                account_name, account_username, account_password))
                            print('\n')
                            print(
                                f"New Detail with account name '{account_name}' and password '{account_password}' has been created \n")
                            print('.......................................................................................')
                        elif log_choice == 2:  
                            print('\n')
                            print(
                                "Here is a list of all your details'accounts in the application")
                            print('.......................................................................................')
                            if display_details():
                                for media in display_details():
                                    print(
                                        f"{media.account_media} Account, username: {media.user_account_username} and password: {media.user_account_password} \n")
                            else:
                                print("Oops! No accounts saved yet!")
                            print('.......................................................................................')
                        elif log_choice == 3: 
                            print("Enter the media name you want to delete")
                            account_name_to_delete = input()
                            if find_details(account_name_to_delete):
                                print(
                                    f"Detail with media name '{account_name_to_delete}' has been deleted")
                                print('\n')
                            else:
                                print('.......................................................................................')
                                print(
                                    f"Detail with media name '{account_name_to_delete}' does not exist")
                                print('.......................................................................................')
                        elif log_choice == 4:  
                            print("You have successfully Signed out")
                            print('.......................................................................................')
                            break
                        else: 
                            print("No such media exists!")

            else:
                print('Enter valid Details')
        elif short_code == 'ex':
            print("Thank you for using our app, Bye!")
            break

if __name__ == '__main__':
    main()




