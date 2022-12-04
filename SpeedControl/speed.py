import tkinter as tk
from tkinter import simpledialog
# Import module
from tkinter import *


class SpeedInputText(object):
    def speedTextbox():
        ROOT = tk.Tk()

        ROOT.withdraw()
        # the input dialog
        SPEEDUSER_INP = simpledialog.askstring(
            title="Change speed", prompt="Choose speed value:")
        return SPEEDUSER_INP


"""
class SpeedInputDropdown(object):
    # Create object
    root = Tk()

    # Adjust size
    root.geometry("200x200")

    # Dropdown menu options
    options = [
        "Slow",
        "Slowish",
        "Normal",
        "Hardish",
        "Hard",
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

    if (clicked.get == "Slow"):
        SpeedChange(15)
    elif (clicked.get == "Slowish"):
        SpeedChange(20)
    elif (clicked.get == "Normal"):
        SpeedChange(25)
    elif (clicked.get == "Hardish"):
        SpeedChange(30)
    elif (clicked.get == "Hard"):
        SpeedChange(35)
"""
