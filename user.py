import pyperclip
class User:
    """
    Class that generates new instances of user's information
    """
    
    user_list =[]

    def __init__(self,lockname,password):

        self.lockname = lockname
        self.password = password

    def save_user(self):

        '''
        save_user method saves user's information objects into user_list
        '''

        User.user_list.append(self)

    def delete_user(self):
        '''
        function to   delete user instance
        '''
        User.user_list.remove(self)
