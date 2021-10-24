import random
import string


class Details():
    user_details = []

    def __init__(self, account_media, user_account_username, user_account_password):
        '''
            Function to initialize user details.
        '''
        self.account_media = account_media
        self.user_account_username = user_account_username
        self.user_account_password = user_account_password

    def save_details(self):
        '''
            Function to save details into user_details.
        '''
        Details.user_details.append(self)

    def delete_details(self):
        '''
            Function to delete saved detail from the user_details.
        '''
        Details.user_details.remove(self)

    @classmethod
    def find_by_account_media(cls, account_media):
        '''
            Method to take and return details that match the account_name.
        '''
        for details in cls.user_details:
            if details.account_media == account_media:
                return details
        return False

    @classmethod
    def display_details(cls):
        '''
            Method to return and display the all details.
        '''
        return cls.user_details

    @classmethod
    def generate_password(cls, password_length):
        '''
           Method to generate random password for a user creating a new account in the the user_details.
        '''
        password = string.ascii_uppercase + string.ascii_lowercase + string.digits + "~!@#$%^&*<?>"
        return ''.join(random.choice(password) for i in range(stringLength))