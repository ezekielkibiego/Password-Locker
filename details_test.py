import unittest
from details import Details


class TestDetails(unittest.TestCase):
    def setUp(self):
        '''
            Setup method for the testing initial details.
        '''
        self.new_details = Details(
            "Facebook", "ekibiego", "kib0733")

    def test_init(self):
        '''
            Test to check if the details object has been created.
        '''
        self.assertEqual(self.new_details.account_media, "Facebook")
        self.assertEqual(
            self.new_details.user_account_username, "ekibiego")
        self.assertEqual(
            self.new_details.user_account_password, "kib0733")

    def test_save_details(self):
        '''
        test to check if the details object is saved to the user_details.
        '''
        self.assertEqual(len(Details.user_details), 0)
        self.new_details.save_details()
        self.assertEqual(len(Details.user_details), 1)

    def test_delete_details(self):
        '''
        to check if a saved detail from the user_details is deleted.
        '''
        self.assertEqual(len(Details.user_details), 0)
        self.new_details.save_details()
        self.assertEqual(len(Details.user_details), 1)
        self.new_details.delete_details()
        self.assertEqual(len(Details.user_details), 0)

    def test_find_credentials_by_media(self):
        '''
        test to check if we can find a detail by account media.
        '''
        self.found_details = Details.find_by_account_media(
            "Facebook")



if __name__ == '__main__':
    unittest.main()


