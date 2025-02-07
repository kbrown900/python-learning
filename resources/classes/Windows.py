from tkinter import Toplevel, Label, Button

class NewWindow:     

    def __init__(self, parent_window, title, menu_bar, message):
        self.new_window = Toplevel(parent_window)
        self.new_window.title(title)
        self.new_window.geometry('350x200')
        self.new_window.iconbitmap("resources/images/Support_Icon.ico")
        self.add_widgets(message)
        self.new_window.config(menu=menu_bar)

    def add_widgets(self, message):
        self.label = Label(self.new_window, text=message )
        self.label.pack()

        button = Button(self.new_window, text="Close", command=self.new_window.destroy)
        button.pack()