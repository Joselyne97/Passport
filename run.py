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

def save_account(account):
    '''
    Function to save the user's accounts
    '''
    account.save_account()

def del_account(account):
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
                print("Kindly use these short codes : \n nac - create a new account, \n lo: to login, \n ex: exit account list")

                short_code = input('Choose a short code').lower().strip()

                if short_code == 'ex':
                    break
                elif short_code == 'nac':

                    print("New Account")
                            print("."*40)
                            print(' ')
                            print ("To be a new user")
                            f_name = input()

                            print("Last name ...")
                            l_name = input()

                            print("Phone number ...")
                            p_number = input()

                            print("Email address ...")
                            e_address = input()


                            save_contacts(create_contact(f_name,l_name,p_number,e_address)) # create and save new contact.
                            print ('\n')
                            print(f"New Contact {f_name} {l_name} created")
                            print ('\n')

                    elif short_code == 'dc':

                            if display_contacts():
                                    print("Here is a list of all your contacts")
                                    print('\n')

                                    for contact in display_contacts():
                                            print(f"{contact.first_name} {contact.last_name} .....{contact.phone_number}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any contacts saved yet")
                                    print('\n')

                    elif short_code == 'fc':

                            print("Enter the number you want to search for")

                            search_number = input()
                            if check_existing_contacts(search_number):
                                    search_contact = find_contact(search_number)
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
