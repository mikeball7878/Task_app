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

filename = "login_dict.json"

def load_convert():
    """
    Opens file login_dict.json converts strings in to list of dictionaries and returns the list
    """

    try:
        with open(filename, "r") as file:
            login_string = file.read()
        login_list = json.loads(login_string)
        return login_list
    except FileNotFoundError:
        print("file not found")

''' if login_data:
            for i in range(len(login_data)):
                login_data_dict = ast.literal_eval(login_data[i])
                login_dict_list.append(login_data_dict)
            return login_dict_list
        else:
            return 'empty'
'''

def convert_write(dict_list):
    """ Converts list of dictionaries to strings and writes to 'filename' """

    try:
        with open(filename, "w") as file:
            json.dump(dict_list, file)
    except FileNotFoundError:
        print("file not found")



'''' tasks_dict_list = dict_list
    for i in range(len(tasks_dict_list)):
        data_list.append(str(tasks_dict_list[i]))
    for i in range(len(data_list)):
        data_list[i] = data_list[i] + '\n'
    with open(filename, "w") as file:
        for i in range(len(data_list)):
            file.writelines(data_list[i])
'''

def sign_up():
    print(" Sign up for new account")
    user_name = input("Enter your user name: ")
    password = getpass.getpass()
    login_dict_list = load_convert()
    print(f" password and username  {password}, {user_name}")

    for i in range(len(login_dict_list)):
        if login_dict_list[i].get("user") == user_name:
            print(f" {user_name} user name already exists ")
            sign_up()

    if login_dict_list != 'empty':
        login_obj = {"user": user_name, "P_word": password}
        login_dict_list.append(login_obj)
        convert_write(login_dict_list)
    else:
        login_dict_list = []
        login_obj = {"user": user_name, "P_word": password}
        login_dict_list.append(login_obj)
        convert_write(login_dict_list)

def check_login(user_name, password):

    print(f" password and username  {password}, {user_name}")
    login_dict_list = load_convert()

    if login_dict_list != 'empty':
        for i in range(len(login_dict_list)):
            if login_dict_list[i].get("user") == user_name and login_dict_list[i].get("P_word") == password:
                print(f" username {user_name}")
                return "OK"
        print("Login doesn't match \n")
        end_program = input(" Press 'Return' to try again or press 'q' to quit ")
        if end_program == 'q':
            quit()
        else:
            sign_up()
            return None

    else:
        print("Login Data Not Found")
        end_program = input(" press q to quict ")
        if end_program == 'q':
            quit()
        else:
            sign_up()
            return None

def login():

    action = input(" Press 'Enter' to start, q to quit, "
                        "or type 'new' to create a new account: ")
    if action == 'new':
        sign_up()
        return "OK"

    elif action == 'q':
        quit()

    else:
        user_name = input("Enter your username: ")
        password = input("Enter your password: ")
        user_status = check_login(user_name, password)
        print(f" user status   {user_status}")
        if user_status == 'OK':
            return "OK"
        else:
            print ("Login doesn't match ")
        return None

if __name__ == "__main__":
    login()

