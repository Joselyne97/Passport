
import pyperclip
from account-user import User, Account

def create_user(myname,mypassword):
    '''
    Function to create a new user's account
    '''
    new_user = User(myname,mypassword)
    return new_user

def save_user(user):
    '''
    Function to save the user
    '''
    user.save_user()

def verify_user(lockname,password):
    '''
    function that verifies the existance of user
    '''
    checking_user = Account.check_user(lockname,password)
    return checking_user

def generate_newpassword():
    '''
    function to generate password
    '''
    gen_pass = Account.generate_newpassword()
    return gen_pass  

def create_account(somedia,username,accpassword):
    '''
    Function to add a new social media's account
    '''
    new_account = Account(somedia,username,accpassword)
    return new_account

def save_account(account):
    '''
    Function to save the user's accounts
    '''
    account.save_account()

# def delete_account(account):
#     '''
#     Function to delete a the unwanted social media's account
#     '''
#     account.delete_account()

def display_accounts(somedia):
    '''
    Function that returns all the saved accounts
    '''
    return Account.display_accounts(somedia)

def copy_account(somedia):
    '''
    function to copy account
    '''
    return Account.copy_account(somedia)

def main():
    print(' ')
    print("Hello Welcome to PasswordLocker.")
            # user_name = input()

            # print(f"Hello {user_name}. what would you like to do?")
            # print('\n')

    while True:
        print(' ')
        print('.'*40)
        print("Kindly use these short codes : \n nac = create a new account on password locker, \n lg = to login,  \n dlt = to delete the social media account, \n dc = to display the account list, \n cp = to copy the password, \n ex = exit account list")

        short_code = input('Choose a short code: ').lower().strip()

        if short_code == 'ex':
            break

        elif short_code == 'nac':

            print("."*40)
            print(' ')
            print ("Create a new account:")
            lockname = input('Input the username -').strip()
            password = input('Input the password not less than 8 character').strip()
            save_user(create_user(lockname,password))
            print(f'New user created for: {lockname} using password: {password}')
            

        elif short_code == 'lg':
                print("_"*40)
                print(' ')
                print('to login enter your account details:')
                lockname = input('Enter your lockname orusername - ').strip()
                password= str(input('Enter your password - '))
                user_exists = verify_user(lockname,password)
                if user_exists == lockname:
                    print(" ")
                    print(f'Welcome {lockname} .Please choose any option  to continue.')
                    print(' ')  
                    while True:
                        print("_"*40)
                        print('to navigate to account use code:\n nac = to create an account \n dc = to display accounts \n cy = to copy  password \n dlt = to delete \n ex- Exit')
                        short_code=input('Enter a choice: ').lower().strip()
                        print("_"*40)
                        if short_code =='ex':
                            print(' ')   
                            print(f'Thank you! {lockname}.')
                            break

                        elif short_code == 'dlt':

                            print("_"*40)
                            print(' ')
                            print('Successfully Deleted!')
                            break
                        elif short_code =='nac':
                            print(' ')
                            print('Enter your account name: ')
                            somedia = input('enter the the social media\'s name- ').strip() 
                            username = input('enter your account \'s username - ').strip()
                            
                            while True:
                                print(' ')
                                print("_"*50)
                                print("please enter the choose for entering password for your account: \n pwd = enter existing password \n gp-generate password \n dlt- delete \n ex- Exit")
                                opt_choice = input('Enter an option: ').lower().strip()
                                print("-"*80)
                                if opt_choice == 'pwd':
                                    print(" ")
                                    accpassword = input('enter your password: ').strip()
                                    break
                                
                                elif short_code == 'del':
                                    print("_"*80)
                                    print(' ')
                                    print('Successfully Deleted!')
                                    break
                                
                                elif psw_choice == 'gp':
                                    password = generate_password()
                                    break
                                elif psw_choice == 'ex':
                                    break
                                else:
                                    print('Try Again!.')
                            save_credential(create_credential(user_name,site_name,account_name,password))
                            print(' ')
                            print(f'Credential Created:Site Name:  {site_name} -Acount Name:{account_name} -Password:{password}')
                            print(' ')
                        elif short_code == 'dc':
                            print(' ')
                            if display_credentials(user_name):
                                print('Here is a list of all credentials')
                                print(' ')
                                for credential in display_credentials(user_name):
                                    print(f'Site Name : {credential.site_name} - Account Name: {credential.account_name} - Password: {credential.password}')
                                    print(' ')
                            else:
                                print(' ')
                                print("you don't seem to have any credentials")
                                print(' ')
                    
                        elif short_code =='copy':
                            print(' ')
                            chosen_site = input("enter the site for credential password to copy: ")

                            copy_credential(chosen_site)
                            print(' ')
                        else: 
                            print('TRY Again')
                
                else:
                    print(' ')
                    print('TRY Again or create another account.')

                 
         
            else:
                print("_"*80)
                print(' ')
                print("try Again")

        #     print("Username of the social media's account")
        #     socialusername = input()

        #     print("The password of the social media's account")
        #     socialpassword = input()


        #     save_accounts(create_account(socialaccount,socialusername,socialpassword)) # create and save new social media's information.
        #     print ('\n')
        #     print(f"New Account {socialaccount} {socialpassword} created")
        #     print ('\n')

        # elif short_code == 'dc':

        #         if display_accounts():
        #                 print(' ')
        #                 print("Here is a list of all your accounts")
        #                 print("."*40)
        #                 print('\n')

        #                 for account in display_accounts():
        #                     print(f"{account.socialaccount} {account.socialusername} .....{account.socialpassword}")

        #                     print('\n')
        #         else:
        #                 print('\n')
        #                 print("You dont seem to have any account saved yet")
        #                 print('\n')

        # elif short_code == 'dlt':
        #         if delete_accounts
        #                 print("You want to delete an account")
        #                 print("."*40)
        #                 print(' ')

        #                 print("Enter the social account name you want to delete")

        #                     delete_socialaccount= input()
        #                     if delete_account(socialmedia_name):
        #                             delete_socialaccount = find_account(delete_socialaccount)
        #                             print(f"{delete_account.socialaccount} {delete_account.socialpassword}")
        #                             print('-' * 20)

        #                             print(f"Username of the social media's account{delete_account.username}")
        #                             print(f"The password of the social media's account{delete_account.accpassword}")
        #                     else:
        #                             print("That contact does not exist")

        #             elif short_code == "ex":
        #                     print("Bye .......")
                            break
                    else:
                            print("I really didn't get that. Please use the short codes")
if __name__ == '__main__':

    main()