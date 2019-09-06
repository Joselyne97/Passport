#!/usr/bin/env python3.6

from user import User
from account import Account

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

def create_account(socialaccount,socialusername,socialpassword):
    '''
    Function to add a new social media's account
    '''
    new_account = Account(socialaccount,socialusername,socialpassword)
    return new_account

def save_accounts(account):
    '''
    Function to save the user's accounts
    '''
    account.save_account()

def delete_account(account):
    '''
    Function to delete a the unwanted social media's account
    '''
    account.delete_account()

def display_accounts():
    '''
    Function that returns all the saved accounts
    '''
    return Account.display_accounts()

def main():
    print(' ')
    print("Hello Welcome to your PasswordLocker.")
            # user_name = input()

            # print(f"Hello {user_name}. what would you like to do?")
            # print('\n')

    while True:
        print(' ')
        print('.'*40)
        print("Kindly use these short codes : \n nac - add a new account, \n dlt: to delete the social media account, \n dc: to display the account list, \n ex: exit account list")

        short_code = input('Choose a short code').lower().strip()

        if short_code == 'ex':
            break

        elif short_code == 'nac':

            print("New Account")
            print("."*40)
            print(' ')
            print ("New social media account")
            socialaccount = input()

            print("Username of the social media's account")
            socialusername = input()

            print("The password of the social media's account")
            socialpassword = input()


            save_accounts(create_account(socialaccount,socialusername,socialpassword)) # create and save new social media's information.
            print ('\n')
            print(f"New Account {socialaccount} {socialpassword} created")
            print ('\n')

        elif short_code == 'dc':

                if display_accounts():
                        print(' ')
                        print("Here is a list of all your accounts")
                        print("."*40)
                        print('\n')

                        for account in display_accounts():
                            print(f"{account.socialaccount} {account.socialusername} .....{account.socialpassword}")

                            print('\n')
                else:
                        print('\n')
                        print("You dont seem to have any account saved yet")
                        print('\n')

        elif short_code == 'dlt':
                if delete_accounts
                        print("You want to delete an account")
                        print("."*40)
                        print(' ')

                        print("Enter the social account name you want to delete")

                            socialmedia_name= input()
                            if delete_account(socialmedia_name):
                                    socialmedia_name = delete_account(search_number)
                                    print(f"{search_contact.first_name} {search_contact.last_name}")
                                    print('-' * 20)

                                    print(f"Phone number.......{search_contact.phone_number}")
                                    print(f"Email address.......{search_contact.email}")
                            else:
                                    print("That contact does not exist")

                    elif short_code == "ex":
                            print("Bye .......")
                            break
                    else:
                            print("I really didn't get that. Please use the short codes")
