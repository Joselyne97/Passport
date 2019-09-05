import unittest
from credential import Account

class testAccounts(unittest.TestCase):
    '''
    Test class that defines test cases for the account class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''      
        Set up method to run before each test cases.
        '''
        self.new_account = Account("Github","Joselyne97","jojopass") # create contact object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_account.account_name,"Github")
        self.assertEqual(self.new_account.username,"Joselyne97")
        self.assertEqual(self.new_account.account_password,"jojopass")

    def test_save_account(self):
        '''
        test_save_account test case to test if the account object is saved into
         the account list
        '''
        self.new_account.save_account() # saving the new contact
        self.assertEqual(len(Account.account_list),1)

if __name__ == '__main__':
    unittest.main()