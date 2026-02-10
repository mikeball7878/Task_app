
# program to track tasks. Tasks are stored in a separate file: tasks.txt
# Uses login_prog.py to handle login and passwords stored in a separate file: login_dict.json
from icecream import ic

import ast
from _pyrepl.completing_reader import complete
import json

from login_prog import login


def getAction():
    try:
        user_input = int(input("Pick a number:\n 1 - Add task \n 2 - View Tasks \n 3 - Mark Task Complete "
                "\n 4 - Delete Task \n 5 - Logout \n You Picked: "))
        if user_input < 1 or user_input > 5:
            print("Enter a number between 1 and 5")
        else:
            return user_input
    except ValueError:
        print("Enter a valid number")

def load_convert():
    # opens file task.txt converts strings in to list of dictionaries and returns the list
    tasks_dict_list = []
    with open("tasks.txt", "r") as file:
        task_data = file.read().splitlines()
        if task_data:
            for i in range(len(task_data)):
                tasks_data_dict = ast.literal_eval(task_data[i])
                tasks_dict_list.append(tasks_data_dict)
            return tasks_dict_list
        else:
            return 'empty'


def convert_write(dict_list):
    # converts list of dictionaries to strings and writes to file task.txt
    tasks_data_list = []
    tasks_dict_list = dict_list
    for i in range(len(tasks_dict_list)):
        tasks_data_list.append(str(tasks_dict_list[i]))
    for i in range(len(tasks_data_list)):
        tasks_data_list[i] = tasks_data_list[i] + '\n'
    with open("tasks.txt", "w") as file:
        for i in range(len(tasks_data_list)):
            file.writelines(tasks_data_list[i])
    return


def main():
    if login() == "OK":
        print("Logged in")
    else:
        print("Login failed")
        login()

    while True:
        action = getAction()
        match action:
            case 1:   #  Add Task
                task = input(" Enter the task: ")
                tasks_dict_list = load_convert()
                if tasks_dict_list != 'empty':
                    old_index = tasks_dict_list[-1].get("Task #")
                    task_obj = {'Task #': old_index + 1, 'Status': 'pending', 'Description': task}
                    tasks_dict_list.append(task_obj)
                    print(f" Task #:", old_index + 1, " added to list" "\n")
                    convert_write(tasks_dict_list)
                else:
                    tasks_dict_list = []
                    task_obj = {'Task #': 1, 'Status': 'pending', 'Description': task}
                    tasks_dict_list.append(task_obj)
                    convert_write(tasks_dict_list)

            case 2:  #  View tasks
                tasks_dict_list = load_convert()
                if tasks_dict_list != 'empty':
                    for i in range(len(tasks_dict_list)):
                        print(f" Task #:", tasks_dict_list[i].get("Task #"),
                              "  Status:", tasks_dict_list[i].get("Status"), "\n",
                              "Description:",tasks_dict_list[i].get("Description"), "\n")
                else:
                    print("No current tasks \n")

            case 3:   #  Mark Task as complete
                tasks_dict_list = load_convert()
                if tasks_dict_list != 'empty':
                    task_to_mark_complete = int(input("Enter the task to mark complete: "))
                    for i in range(len(tasks_dict_list)):
                        task_id = tasks_dict_list[i].get("Task #")
                        if task_to_mark_complete == task_id:
                            tasks_dict_list[i]['Status'] = 'complete'
                            break
                    convert_write(tasks_dict_list)
                else:
                    print("No current tasks \n")

            case 4:   # Delete Task
                try:
                    tasks_dict_list = load_convert()
                    if tasks_dict_list != 'empty':
                        task_to_delete = int(input("Enter the task to delete: "))
                        for i in range(len(tasks_dict_list)):
                            task_id = tasks_dict_list[i].get("Task #")
                            if task_to_delete == task_id:
                                tasks_dict_list.remove(tasks_dict_list[i])
                                break
                        convert_write(tasks_dict_list)
                    else:
                        print("No current tasks \n")
                except ValueError:
                    print(" Enter a valid number")

            case 5:
                quit()
main()

