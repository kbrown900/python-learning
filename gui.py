from tkinter import *
from resources.classes.Windows import NewWindow

# Main Application Class
class MainApp:
    def __init__(self, root):
        self.window = root
        self.window.title("Hello World")
        self.window.geometry('350x200')
        self.window.iconbitmap("resources/images/Support_Icon.ico")
        
        # Set up menu bar
        self.menu_bar = self.setup_menu()

        # Add content to the main window
        self.lbl = Label(self.window, text="Test Words for input")
        self.lbl.grid()

        # Entry Field
        self.txt = Entry(self.window, width=10)
        self.txt.grid(column=1, row=0)

        # Buttons
        self.setup_buttons()

    def setup_menu(self):
        # Menu bar
        menu_bar = Menu(self.window)

        # Create menu
        menu_1 = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label='File', menu=menu_1)
        menu_1.add_command(label='New', command=self.reset)
        menu_1.add_separator()
        menu_1.add_command(label='Exit', command=self.closeProgram)

        help_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Help",menu=help_menu)
        help_menu.add_command(label="About", command=self.show_about)
        help_menu.add_command(label="Documentation", command=self.show_documentation)
        self.window.config(menu=menu_bar)
        return menu_bar

    def setup_buttons(self):
        # Configure buttons
        btn = Button(self.window, text="Click Here", fg="red", command=self.clicked)
        btn_reset = Button(self.window, text="Reset", fg="Black", command=self.reset)
        btn_close = Button(self.window, text='Close', fg="Black", command=self.closeProgram)
        btn_createwindow = Button(self.window, text="New Window", fg="Black", command=self.createWindow)

        # Set buttons to grid
        btn.grid(column=1, row=1)
        btn_reset.grid(column=2, row=1)
        btn_close.grid(column=1, row=2)
        btn_createwindow.grid(column=1, row=3)

    # Button functions
    def clicked(self):
        result = "You wrote: " + self.txt.get()
        self.lbl.configure(text=result)
        self.txt.delete(0, END)

    def reset(self):
        self.txt.delete(0, END)
        self.lbl.configure(text="Test Words for input")

    def closeProgram(self):
        self.window.quit()

    def show_about(self):
        about_message = "This is a test of the About Section\nso now I will keep testing"
        NewWindow(self.window, "About", self.menu_bar, about_message)

    def show_documentation(self):
        doc_message = "This is a test of the Documentation Section"
        NewWindow(self.window, "Documentation", self.menu_bar, doc_message)    

    # Function to create a new window
    def createWindow(self):
        # Pass the main app window to NewWindow
        NewWindow(self.window, "New Window", self.menu_bar, "This is a new window")

# Main entry point
if __name__ == "__main__":
    # Create the main window
    root = Tk()
    app = MainApp(root)
    
    # Start the main loop
    root.mainloop()
