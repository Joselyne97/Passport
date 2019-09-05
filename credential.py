class Account:
    """
    Class that generates new instances of user's accounts
    """
    
    account_list =[]
    
    def __init__(self,account_name,username,account_password):

        self.account_name = account_name
        self.username = username
        self.account_password = account_password

    def save_account(self):

        '''
        save_account method saves account objects into account_list
        '''

        Account.account_list.append(self)

    def delete_account(self):

        '''
        delete_account method deletes a saved account from the account_list
        '''

        Account.account_list.remove(self)

