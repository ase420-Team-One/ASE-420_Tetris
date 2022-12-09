import tkinter as tk
from tkinter import simpledialog
# Import module
from tkinter import *

class GridInputText(object):
    def gridTextbox():
        # we need pressing_down, fps, and counter to go_down() the Tetris Figure
        ROOT = tk.Tk()

        ROOT.withdraw()
        # the input dialog
        ROWUSER_INP = simpledialog.askstring(
            title="Change grid row size", prompt="Change grid row size")
        COLUMNUSER_INP = simpledialog.askstring(
            title="Change grid column size", prompt="Change grid column size")
        return [ROWUSER_INP, COLUMNUSER_INP]


grid_dict= {
    "Large" : (600, 700),
    "Largish": (500, 600),
    "Normal": (400, 500),
    "Smallish": (300, 400),
    "Small": (200, 300),
}



"""
class GridInputDropdown(object):
    # Create object
    root = Tk()

    # Adjust size
    root.geometry("200x200")

    # Dropdown menu options
    options = [
        "Large",
        "Largish",
        "Normal",
        "Smallish",
        "Small",
    ]

    # datatype of menu text
    clicked = StringVar()

    # initial menu text
    clicked.set("Normal")

    # Create Label
    label = Label(root, text=" ")
    label.pack()

    # Change the label text
    def show(self, label, clicked):
        label.config(text=clicked.get())

    # Create Dropdown menu
    drop = OptionMenu(root, clicked, *options)
    drop.pack()

    # Create button, it will change label text
    button = Button(root, text="Enter", command=show).pack()

    # Execute tkinter
    root.mainloop()

    if (clicked.get == "Large"):
        GridChange((600, 700))
    elif (clicked.get == "Largish"):
        GridChange((500, 600))
    elif (clicked.get == "Medium"):
        GridChange((400, 500))
    elif (clicked.get == "Smallish"):
        GridChange((300, 400))
    elif (clicked.get == "Small"):
        GridChange((200, 300))
"""
