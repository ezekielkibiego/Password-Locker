import unittest
from details import Credentials

class TestCredentials(unittest.TestCase):
    def setUp(self):
        '''
            Setup method for the testing initial credentials.
        '''
        self.new_credentials = Credentials(
            "Facebook", "ekibiego", "kib0733")

    def test_init(self):
        '''
            Test to check if the credentials object has been created
        '''
        self.assertEqual(self.new_credentials.account_name, "Facebook")
        self.assertEqual(
            self.new_credentials.user_account_username, "ekibiego")
        self.assertEqual(
            self.new_credentials.user_account_password, "kib0733")

    def test_save_credentials(self):
        '''
        test to check if the credentials object is saved to the user_credentials.
        '''
        self.assertEqual(len(Credentials.user_credentials), 0)
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.user_credentials), 1)

    def test_delete_credentials(self):
        '''
        to check if a saved credential from the user_credentials is deleted.
        '''
        self.assertEqual(len(Credentials.user_credentials), 0)
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.user_credentials), 1)
        self.new_credentials.delete_credentials()
        self.assertEqual(len(Credentials.user_credentials), 0)

    def test_find_credentials_by_name(self):
        '''
        test to check if we can find a credential by account name.
        '''
        self.found_credentials = Credentials.find_by_account_name(
            "Facebook")



if __name__ == '__main__':
    unittest.main()


