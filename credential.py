class Account:
    """
    Class that generates new instances of user's accounts
    """
    
    account_list =[]
    
    def __init__(self,somedia,username,accpassword):

        self.somedia = somedia
        self.username = username
        self.accpassword = accpassword

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

    # @classmethod
    # def find_by_accountname(cls,accountname):
    #     '''
    #     Method that takes in a name and returns an account's name that matches that username.

    #     Args:
    #         accountname: the somedia account to search for
    #     Returns :
    #         password of a social media that matches the accountname.
    #     '''

    #     for account in cls.account_list:
    #         if account.somedia == accountname:
    #             return account


    @classmethod
    def display_accounts(cls):
        '''
        method that returns the account list
        '''
        return cls.account_list

        