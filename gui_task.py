import login_prog
FILENAME = "task_dict.json"

import FreeSimpleGUI as sg

label = sg.Text("Input Task Description")

input_box = sg.InputText(tooltip="Enter Task", key="task")

add_button = sg.Button("Add Task")

window = sg.Window("Task Manager", layout=[[label],[input_box,add_button]],
                   font=("Helvetica", 15))
while True:
    event, values = window.read(timeout=50000)
    print(event)
    match event:
        case "Add Task":
            tasks = login_prog.retrieve_dict(FILENAME)
            new_task = values['task'] + "/n"
            tasks.append(new_task)
            login_prog.save_dict(tasks, FILENAME)
        case sg.WIN_CLOSED:
            break


window.close()

