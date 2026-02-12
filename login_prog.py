'''
This is a set of functions that handle the username and password requirements
for the main.py task module. File task_dict.json stores the login data.
That file should be encrypted but hasn't happened yet.  The getpass module is
imported for the hiding of the password characters.  The json module is
imported for converting text data into dictionaries.
'''

import getpass
import json

LOGIN_FILE = "login_dict.json"

def retrieve_dict(file_name):
    """  Opens file login_dict.json and converts strings in to list of dictionaries
    and returns the list.
    """
    try:
        with open(file_name, "r") as file:
            login_string = file.read()
            if login_string:
                login_list = json.loads(login_string)
            else:
                return "empty"
        return login_list
    except FileNotFoundError:
        print("file not found")

def save_dict(dict_list, file_name):
    """ Converts list of dictionaries to strings and writes to 'FILENAME'
    """
    try:
        with open(file_name, "w") as file:
            json.dump(dict_list, file)
    except FileNotFoundError:
        print("file not found")

def add_user(user_name, password):
    """ Creates the login dictionary, retrieves the old dictionary
     and saves new one to 'FILENAME'
    """
    login_obj = {"user": user_name, "P_word": password}
    dict_list = retrieve_dict(LOGIN_FILE)
    if dict_list != "empty":
        dict_list.append(login_obj)
        save_dict(dict_list, LOGIN_FILE)
    else:
        dict_list = [login_obj]
        save_dict(dict_list, LOGIN_FILE)

def get_name_password():

    user_name = input("Enter your user name: ")
    print("Enter your password. Password chars are hidden")
    password = getpass.getpass()
    return user_name, password

def check_user_name (user_name):
    """ Checks if any username and password data exist, then checks if
    username already exists in the login dictionary
    """
    dict_list = retrieve_dict(LOGIN_FILE)
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
    """ Checks if any username and password data exist and then verifies
    they match
    """
    login_dict_list = retrieve_dict(LOGIN_FILE)
    if login_dict_list != 'empty':
        for i in range(len(login_dict_list)):
            if login_dict_list[i].get("user") == user_name and login_dict_list[i].get("P_word") == password:
                print(f"Username: {user_name}")
                return "OK"
        return "Wrong password or username"
    else:
        print("Login Data Not Found")
        return  "no data found"

def login():
    """ This is the main function that manages all the other functions.
    It is called by main.py to log the user in for task management
    """
    action = input("Press 'Enter' to login, q to quit,"
                        "or type 'new' to create a new account: ")
    if action == 'new':
        print("Sign up for new account")
        name, password = get_name_password()
        user_status = check_user_name(name)
        if user_status == 'OK':
            add_user(name, password)
            print("Sign up successful ")
            return "OK"
        else:
            login()

    elif action == '':    # pressing return by the user
        print("Log In")
        name, password = get_name_password()
        user_status = check_login(name, password)
        if user_status == 'OK':
            print("Login successful ")
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

