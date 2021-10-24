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

    def test_find_user(self):
        '''
        function to test if the user account exists in the user list
        '''
        self.found_user = User.find_user("kezekiel")


    def test_user_exists(self):
        '''
        Function to test the user account exists in the user list
        '''
        self.found_user = User.user_exist("kezekiel")




if __name__ == '__main__':
    unittest.main()

