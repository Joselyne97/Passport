#!/usr/bin/env python3.6

from user import User
from credential import Account

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
    contact.save_user()

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
    contact.save_account()




