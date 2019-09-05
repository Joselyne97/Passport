class User:
    """
    Class that generates new instances of user's information
    """
    
    user_list =[]

    def __init__(self,first_name,last_name,lockname,password):

        self.first_name = first_name
        self.last_name = last_name
        self.lockname = lockname
        self.password = password

    def save_user(self):

        '''
        save_user method saves user's information objects into user_list
        '''

        User.user_list.append(self)