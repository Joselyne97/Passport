import unittest
from user import User

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
        self.assertEqual(len(User.user_list),1)


if __name__ == '__main__':
    unittest.main()