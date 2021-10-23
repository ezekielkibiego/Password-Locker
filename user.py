class User():

    user_list = []

    def __init__(self, username, password):
        '''
        Method to initialize the user.
        '''
        self.username = username
        self.password = password

    def save_user(self):
        '''
        method to save user to the list.
        '''
        User.user_list.append(self)

    def delete_user(self):
        '''
        Method to delete user from the list.
        '''
        User.user_list.remove(self)
