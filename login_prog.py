# Program to get user input to create user name and password if required.
# Program will also check for proper login and password.
# text based interface and file management.  Data is stored in login_dict.json

import getpass
import json

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
    else:
        dict_list = [login_obj]
        save_dict(dict_list)

def get_name_password():

    print(" ")
    user_name = input("Enter your user name: ")
    print("Enter your new password. Password chars are hidden")
    password = getpass.getpass()
    return user_name, password

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
        return 'OK'

def check_login(user_name, password):

    login_dict_list = retrieve_dict()
    if login_dict_list != 'empty':
        for i in range(len(login_dict_list)):
            if login_dict_list[i].get("user") == user_name and login_dict_list[i].get("P_word") == password:
                print(f" username {user_name}")
                return "OK"
            else:
                return "Wrong password or username"
    else:
        print("Login Data Not Found")
        return  "no data found"

def login():

    action = input(" Press 'Enter' to login, q to quit,"
                        "or type 'new' to create a new account: ")
    if action == 'new':
        print("Sign up for new account")
        name, password = get_name_password()
        user_status = check_user_name(name, password)
        if user_status == 'OK':
            add_user(name, password)
            print("Sign up successful ")
            return "OK"
        else:
            logi

    elif action == '':
        print("Log In")
        name, password = get_name_password()
        user_status = check_login(name, password)
        if user_status == 'OK':
            print("login successful ")
            return "OK"
        else:
            print("Login doesn't match")
            login()

    elif action == 'q':
        quit()

    else:
        print("Invalid input")
        login()

if __name__ == "__main__":
    login()

