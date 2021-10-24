#!/usr/bin/env python3.8
from user import User
from details import Credentials

def function():
	print("               ____                        _ ")
	print("              |  _ \                      | |")
	print("              |  __/  / _  |/ __  / __    | |")
	print("              | |    / (_| |\__ \ \__ \   | |")
	print("              |_|    \_____| ___/  ___/   |_| ")
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
def find_existing_user(username):
    '''
    find if user exists
    '''
    return User.user_exist(username)
def find_user_password(username, password):
    '''
    find if the user enter the correct username and password
    '''
    return User.find_user(username, password)
def create_new_credential(account_name, account_username, account_password):
    '''
    create a new credential
    '''
    new_credential = Credentials(
        account_name, account_username, account_password)
    return new_credential
def save_credentials(credentials):
    '''
    save credentials
    '''
    credentials.save_credentials()
def display_credentials():
    """
    display credentials
    """
    return Credentials.display_credentials()
def delete_credential(account_name):
    '''
    delete credentials
    '''
    return Credentials.delete_credentials(account_name)
def find_credential(account_name):
    '''
    find credentials
    '''
    return Credentials.find_by_account_name(account_name)
def generate_password(password_length):
    """
    generate a random password
    """
    return Credentials.generate_password(password_length)

def main():
    print("Hi, What is your name?")
    name = input()
    while True:
        print('*'*100)
        print(f"Welcome {name} ...\n kindly, use the following to proceed.\n ca ...  Create New Account \n fa ...  Find Account  \n lg ... to login to your account  \n da ... display account \n ex ... exit from app")
        print('*'*100)
        short_code=input("").lower().strip()

        if short_code == 'ca':
            print("Create New User Account")
            print('*'*100)
            print("Enter your username .....")
            username = input()
            print("Enter password .....")
            password = input()
            save_user(create_new_user(
                      username, password))
            print('*'*100)
            print(
                f"Bravo! {name}. You've created Account successfully. lg to login to your account")
            print('*'*100)

        elif short_code == 'lg' or short_code == 'da':
            print('*'*100)
            print("Enter your username ...")
            username = input()
            print("Enter your password ...")
            password = input()
        
        
        elif short_code == 'ex':
            print("Thank you for using our app, Bye!")
            break

if __name__ == '__main__':
    main()




