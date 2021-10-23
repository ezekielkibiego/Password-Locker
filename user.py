class User():

    user_list = []

    def __init__(self, username, password):
        """
        Initialize the user.
        """
        self.username = username
        self.password = password

    def save_user(self):
        """
        Save user to list.
        """
        User.user_list.append(self)

    def delete_user(self):
        """ 
        Delete user from the list
        """
        User.user_list.remove(self)
