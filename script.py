import tkinter as tk
from tkinter import messagebox

def create_ui(ast):
    root = tk.Tk()
    for element in ast["elements"]:
        if element["type"] == "Window":
            setup_window(root, element)
    root.mainloop()

def setup_window(root, window):
    root.title(window["attributes"]["title"])
    root.geometry(f'{window["attributes"]["size"][0]}x{window["attributes"]["size"][1]}')
    for child in window["children"]:
        if child["type"] == "Button":
            setup_button(root, child)
        elif child["type"] == "Input":
            setup_input(root, child)

def setup_button(root, button):
    btn = tk.Button(root, text=button["attributes"]["text"], command=lambda: execute_action(button["attributes"]["action"]))
    btn.place(x=button["attributes"]["position"][0], y=button["attributes"]["position"][1])

def setup_input(root, input_field):
    entry = tk.Entry(root)
    entry.insert(0, input_field["attributes"]["placeholder"])
    entry.place(x=input_field["attributes"]["position"][0], y=input_field["attributes"]["position"][1])
    input_field["element"] = entry

def execute_action(action):
    if "show_message" in action:
        message = action.split("show_message(")[1].rstrip(")").strip("'")
        messagebox.showinfo("Info", message)

# Beispiel-AST
ast = {
    "type": "Program",
    "elements": [
        {
            "type": "Window",
            "name": "main",
            "attributes": {"title": "Meine App", "size": [800, 600]},
            "children": [
                {"type": "Button", "attributes": {"text": "Klick mich!", "position": [100, 100], "action": "show_message('Hallo, Welt!')"}}
            ]
        }
    ]
}

create_ui(ast)
