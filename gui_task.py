import login_prog

import FreeSimpleGUI as sg

label = sg.Text("Input Task Description")

input_box = sg.InputText(tooltip="Enter Task")

add_button = sg.Button("Add Task")

window = sg.Window("Task Manager", layout=[[label],[input_box,add_button]])

window.read(timeout=50000)



window.close()
