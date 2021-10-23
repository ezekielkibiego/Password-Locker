import unittest
from user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        """
        method for the test class to create a new user
        """
        self.new_user = User("ezekiel", "22ezekiel")

    def test_user_created(self):
        """
        Test to check if the user object is created successfully
        """
        self.assertEqual(self.new_user.username, "ezekiel")
        self.assertEqual(self.new_user.password, "22ezekiel")

    def test_user_save(self):
        """
        check if the user object is saved to the user accounts list
        """
        self.assertEqual(len(User.user_list), 0)
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)

    def test_delete_user(self):
        """
        method to check if the user was removed from the user accounts list
        """
        self.assertEqual(len(User.user_list), 0)
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)
        self.new_user.delete_user()
        self.assertEqual(len(User.user_list), 0)


if __name__ == '__main__':
    unittest.main()

