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
        self.new_user = User("Joselyne","Jojo","Joselyne97","jojo11") # create contact object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name,"Joselyne")
        self.assertEqual(self.new_user.last_name,"Jojo")
        self.assertEqual(self.new_user.lockname,"Joselyne97")
        self.assertEqual(self.new_user.password,"jojo11")


if __name__ == '__main__':
    unittest.main()