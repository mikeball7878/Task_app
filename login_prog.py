# Program to get user input to create user name and password if required.
# Program will also check for proper login and password.
# text based interface and file management.  Data is stored in login_dict.json

import ast
from _pyrepl.completing_reader import complete
from enum import nonmember

import getpass
import json
import ast
from xml.etree.ElementInclude import FatalIncludeError

FILENAME = "login_dict.json"

def retrieve_dict():
    """
        Opens file login_dict.json converts strings in to list of dictionaries
     and returns the list.
    """

    try:
        with open(FILENAME, "r") as file:
            login_string = file.read()
            if login_string:
                login_list = json.loads(login_string)
            else:
                print( "empty file")
                return "empty"
        return login_list
    except FileNotFoundError:
        print("file not found")

def save_dict(dict_list):
    """ Converts list of dictionaries to strings and writes to 'filename' """

    try:
        with open(FILENAME, "w") as file:
            json.dump(dict_list, file)
    except FileNotFoundError:
        print("file not found")

def add_user(user_name, password):

    login_obj = {"user": user_name, "P_word": password}
    dict_list = retrieve_dict()
    if dict_list != "empty":
        dict_list.append(login_obj)
        save_dict(dict_list)
        print("another user added")
    else:
        dict_list = [login_obj]
        save_dict(dict_list)
        print("new user added")

def sign_up():

    print(" Sign up for new account")
    user_name = input("Enter your user name: ")
    print("Enter your new password. Password chars are hidden")
    password = getpass.getpass()

    answer = check_user_name(user_name, password)
    if answer == 'OK':
        add_user(user_name, password)
        return "OK"
    elif answer == "Bad":
        print("User name bad ")
        action = input(" Press Enter to try again or q to quit ")
        if action == 'q':
            quit()
        else:
            login()
    else:
        add_user(user_name, password)
        return "OK"


def check_user_name (user_name, password):

    dict_list = retrieve_dict()
    if dict_list != 'empty':
        for i in range(len(dict_list)):
            if dict_list[i].get("user") == user_name:
                print(f" {user_name} user name already exists ")
                return "Bad"
            else:
                return "OK"
    else:
        print("No Login data ")



def check_login():

    user_name = input("Enter your user name: ")
    password = input("Enter your password: ")
    print(f" check login password and username  {password}, {user_name}")
    login_dict_list = retrieve_dict()

    if login_dict_list != 'empty':
        for i in range(len(login_dict_list)):
            if login_dict_list[i].get("user") == user_name and login_dict_list[i].get("P_word") == password:
                print(f" username {user_name}")
                return "OK"
            else:
                return "Wrong password or username"
    else:
        return "Login Data Not Found"

def login():

    action = input(" Press 'Enter' to login, q to quit,"
                        "or type 'new' to create a new account: ")
    if action == 'new':
        sign_up()
        print("Sign up successful ")
        return "OK"

    elif action == 'q':
        quit()

    else:
        user_status = check_login()
        print(f" user status   {user_status}")
        if user_status == 'OK':
            print("Login successful")
            return "OK"
        else:
            action = input("Login doesn't match press 'Enter' to try again or press 'q' to quit ")
            if action == 'q':
                quit()
            else:
                check_login()

if __name__ == "__main__":
    login()

