"""
program to track tasks. Tasks are stored in a separate file: task_dict.json
Uses login_prog.py to handle login and passwords stored in a
separate file: login_dict.jsonq
"""
from time import strftime

TASK_FILE = 'task_dict.json'

from login_prog import login, retrieve_dict, save_dict
import time

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


def main():
    now = strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time: ", now)
    login_ok = login()
    if login_ok != "OK":
        print("Login failed")
        login()

    while login_ok == "OK":
        action = getAction()
        match action:
            case 1:   #  Add Task
                task = input(" Enter the task: ")
                tasks_dict_list = retrieve_dict(TASK_FILE)
                old_index = tasks_dict_list[-1].get("Task #")
                task_obj = {'Task #': old_index + 1, 'Status': 'pending', 'Description': task}
                if tasks_dict_list != 'empty':
                    tasks_dict_list.append(task_obj)
                    print(f" Task #:", old_index + 1, " added to list" "\n")
                    save_dict(tasks_dict_list, TASK_FILE)
                else:
                    # tasks_dict_list = []
                    # task_obj = {'Task #': 1, 'Status': 'pending', 'Description': task}
                    # tasks_dict_list.append(task_obj)
                    tasks_dict_list = [task_obj]
                    save_dict(tasks_dict_list, TASK_FILE)

            case 2:  #  View tasks
                tasks_dict_list = retrieve_dict(TASK_FILE)
                if tasks_dict_list != 'empty':
                    for i in range(len(tasks_dict_list)):
                        print(f" Task #:", tasks_dict_list[i].get("Task #"),
                              "  Status:", tasks_dict_list[i].get("Status"), "\n",
                              "Description:",tasks_dict_list[i].get("Description"), "\n")
                else:
                    print("No current tasks \n")

            case 3:   #  Mark Task as complete
                tasks_dict_list = retrieve_dict(TASK_FILE)
                if tasks_dict_list != 'empty':
                    task_to_mark_complete = int(input("Enter the task to mark complete: "))
                    for i in range(len(tasks_dict_list)):
                        task_id = tasks_dict_list[i].get("Task #")
                        if task_to_mark_complete == task_id:
                            tasks_dict_list[i]['Status'] = 'complete'
                            break
                    save_dict(tasks_dict_list, TASK_FILE)
                else:
                    print("No current tasks \n")

            case 4:   # Delete Task
                try:
                    tasks_dict_list = retrieve_dict(TASK_FILE)
                    if tasks_dict_list != 'empty':
                        task_to_delete = int(input("Enter the task to delete: "))
                        for i in range(len(tasks_dict_list)):
                            task_id = tasks_dict_list[i].get("Task #")
                            if task_to_delete == task_id:
                                tasks_dict_list.remove(tasks_dict_list[i])
                                break
                        save_dict(tasks_dict_list, TASK_FILE)
                    else:
                        print("No current tasks \n")
                except ValueError:
                    print(" Enter a valid number")

            case 5:
                quit()
main()

