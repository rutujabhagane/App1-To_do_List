import Functions_module
import PySimpleGUI as sg
import time
import os
if not os.path.exists("todofile.txt"):
    with open("todofile.txt", "w") as file:
        pass

sg.theme('Black')
clock_label = sg.Text(" ",key="currenttime")
label = sg.Text("Type a To-do!!")
input_box = sg.InputText(tooltip="Enter a todo",key ="todo")

list_box = sg.Listbox(values=Functions_module.read_file(), enable_events=True, key='todo_list', size=[45, 10])
add_button = sg.Button("Add")
edit_button = sg.Button("Edit")
complete_button = sg.Button("Completed")
exit_button = sg.Button("Exit")
layout=[[clock_label],[label],[input_box],[list_box],[add_button,edit_button,complete_button,exit_button]]
window_box = sg.Window("TO-DO-APP",layout,font=('Arial',14))




while True:
    event, value = window_box.read(timeout=200)
    window_box["currenttime"].update(value=time.strftime("%b %d,%Y %H:%M:%S"))

    print("This is the event",event)
    print("This is the value",value)
    # print(value['todo_list'][0])
    match event:
        case "Add":
            todos_list = Functions_module.read_file()
            new_todo = value['todo'] + "\n"
            todos_list.append(new_todo)
            Functions_module.write_to_file(todos_list)
            window_box['todo_list'].update(values=todos_list)
            window_box['todo'].update(value=" ")


        case "Completed":
            try:
                complete_todo =value['todo_list'][0]
                todos_list = Functions_module.read_file()
                # todo_index = todos_list.index(complete_todo)
                # todos_list.pop(todo_index)
                todos_list.remove(complete_todo)
                Functions_module.write_to_file(todos_list)
                window_box['todo_list'].update(values=todos_list)
                window_box['todo'].update(value= " ")
            except IndexError:
                sg.popup("Please select an item first", font=("Arial",12))

        case "Edit":
            try:
                edit_todo = value['todo_list'][0]

                new_todo = value['todo']
                todos_list = Functions_module.read_file()
                edit_index = todos_list.index(edit_todo)
                todos_list[edit_index] = new_todo + "\n"
                Functions_module.write_to_file(todos_list)
                window_box['todo_list'].update(values=todos_list)
                window_box['todo'].update(value=" ")
            except IndexError:
                sg.popup("Please select an item first", font=("Arial",12))
        case "Exit":
            exit()

        case 'todo_list':
            update = value['todo_list'][0]
            window_box['todo'].update(value=update)

        case sg.WINDOW_CLOSED:
            break



