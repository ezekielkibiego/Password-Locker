import unittest
from user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        '''
        Function for the test class to create a new user
        '''
        self.new_user = User("kezekiel", "22ezekiel")

    def test_user_created(self):
        '''
        Function to test to check if the user object is created successfully
        '''
        self.assertEqual(self.new_user.username, "kezekiel")
        self.assertEqual(self.new_user.password, "22ezekiel")

    def test_user_save(self):
        '''
        Function to check if the user object is saved to the user accounts list.
        '''
        self.assertEqual(len(User.user_list), 0)
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)

    def test_delete_user(self):
        '''
        Function to check if the user was deleted from the user list list.
        '''
        self.assertEqual(len(User.user_list), 0)
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)
        self.new_user.delete_user()
        self.assertEqual(len(User.user_list), 0)

    @classmethod
    def find_user(cls, username):
        '''
        Method to find user by username.
        '''
        for user in cls.user_list:
            if user.username == username:
                return user

    @classmethod
    def user_exists(cls, username):
        '''
        method to check if user exists
        '''
        for user in cls.user_list:
            if user.username == username:
                return True
        return False

    @classmethod
    def check_user(cls, username, password):
        '''
        Method check if user exists and if password is correct.
        '''
        user = cls.find_user(username)
        if user and user.password == password:
            return True
        return False



if __name__ == '__main__':
    unittest.main()

