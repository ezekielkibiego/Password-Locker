class User():

    user_list = []

    def __init__(self, username, password):
        '''
        Function to initialize the user.
        '''
        self.username = username
        self.password = password

    def save_user(self):
        '''
        Function to save user to the list.
        '''
        User.user_list.append(self)

    def delete_user(self):
        '''
        Function to delete user from the list.
        '''
        User.user_list.remove(self)
    
    def test_find_user(self):
        '''
        function tocheck whether the user account exists in the user accounts list.
        '''
        self.find_user = User.find_user('ezekiel')

    def test_user_exists(self):
        '''
        Function to check if the user's account exists in the user accounts list.
        '''
        self.find_user = User.user_exist('kezekiel')

