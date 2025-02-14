#Imports
from tkinter import Toplevel, Label, Button, Frame
from resources.classes.resources import resource_path

# New Window for About and Documentation Dialog boxes
class NewWindow:     
    def __init__(self, parent_window, title, menu_bar, message):
        self.new_window = Toplevel(parent_window)
        self.new_window.title(title)
        self.new_window.geometry('350x200')
        self.new_window.iconbitmap(resource_path("resources/images/Support_Icon.ico"))
        self.add_widgets(message)
        self.new_window.config(menu=menu_bar)

    def add_widgets(self, message):
        frame = Frame(self.new_window)
        frame.pack(expand=True)

        self.label = Label(frame, text=message, justify="center")
        self.label.pack()

        button = Button(self.new_window, text="Close", command=self.new_window.destroy)
        button.pack(pady=5)