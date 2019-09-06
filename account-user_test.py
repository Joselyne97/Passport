import unittest
import pyperclip
from account-user import User, Account
 

class testUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''      
        Set up method to run before each test cases.
        '''
        self.new_user = User("Joselyne97","jojo11") # create contact object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.lockname,"Joselyne97")
        self.assertEqual(self.new_user.password,"jojo11")

    def test_save_user(self):
        '''
        test_save_user test case to test if the user's object is saved into the user's list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),2)

    def test_delete_user(self):

	    '''
		delete user's account
		'''

	    self.new_user.save_user()

	    test_user=User("Joselyne97","jojo11")
	    test_user.save_user()
	    self.new_user.delete_user()
	    self.assertEqual(len(User.user_list),1)

class testAccounts(unittest.TestCase):
    '''
    Test class that defines test cases for the account class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def test_check_user(self):
    
        '''
		Function to test whether the login in function check_user works as expected
		'''
        self.new_user = User("Joselyne97","jojo11")
        self.new_user.save_user()
        user2 = User('jo-all','jopass')
        user2.save_user()

        for user in User.user_list:
            if user.lockname == user2.lockname and user.password == user2.password:
	            current_user = user.lockname
        return current_user

        self.assertEqual(current_user,Account.check_user(user2.password,user2.lockname))


    def setUp(self):
        '''      
        Set up method to run before each test cases.
        '''
        self.new_account = Account("Github","Joselyne97","jojopass")



    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_account.somedia,"Github")
        self.assertEqual(self.new_account.username,"Joselyne97")
        self.assertEqual(self.new_account.accpassword,"jojopass")

    # def test_save_account(self):
    #     '''
    #     test_save_account test case to test if the account object is saved into
    #      the account list
    #     '''
    #     self.new_account.save_account()
    #     self.assertEqual(len(Account.account_list),1)

    def test_save_accounts(self):
            '''
            test_save_multiple_account to check if we can save multiple account
            objects to our account_list
            '''
            self.new_account.save_account()
            codewars= Account("Codewars","Jojo","user11") 
            codewars.save_account()
            self.assertEqual(len(Account.account_list),2)


    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Account.account_list = []
            user.user_list=[]

    def test_display_accounts(self):
        '''
        method that returns a list of all accounts saved
        '''
        self.new_account.save_account()
        codewars = account('Codewars', 'Jojo','user')
        codewars.save_account()
        gmail= account('Gmail','Joselyne JOJO','jojoly')
        gmail.save_account()
        self.assertEqual(len(Account.display_accounts(codewars.somedia)),2)

    def test_find_by_somedia(self):
        '''
		Test to check if the find_by_somedia method returns the correct account
		'''
        self.new_account.save_account()
        codewars = Account('Codewars','Jojo','user')
        codewars.save_account()
        account_exists = Account.find_by_somedia('Codewars')
        self.assertEqual(account_exists,codewars)



    def test_delete_account(self):
            '''
            test_delete_account to test if we can remove an account from our account list
            '''
            self.new_account.save_account()
            test_account = Account("Codewars","Jojo","user")
            test_account.save_account()

            self.new_account.delete_account()
            self.assertEqual(len(Account.account_list),1)


    def test_copy_account(self):
        '''
		test to check if the copy an account method copies the correct account
		'''
        self.new_account.save_account()
        codewars= Account('Codewars','Jojo','user')
        codewars.save_account()
        find_account = None

        for account in Account.user_account_list:
            find_account=Account.find_by_somedia(account.somedia)
            return pyperclip.copy(find_account.accpassword)

        Account.copy_account(self.new_account.somedia)
        self.assertEqual('jojopass',pyperclip.paste())
        print(pyperclip.paste())

    

    



if __name__ == '__main__':
    unittest.main()