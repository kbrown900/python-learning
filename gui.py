from tkinter import *
from resources.classes.Windows import NewWindow
from resources.classes.guess import GuessingGame

# Main Application Class
class MainApp:
    def __init__(self, root):
        self.window = root
        self.window.title("Games")
        self.window.geometry('225x200')
        self.window.iconbitmap("resources/images/Support_Icon.ico")
        
        # Set up menu bar
        self.menu_bar = self.setup_menu()

        # Add content to the main window0
        self.lbl = Label(self.window, text="Select a game to play")
        self.lbl.grid(column=1,row=0, pady=10)

        # Buttons
        self.setup_buttons()

    def setup_menu(self):
        # Menu bar
        menu_bar = Menu(self.window)

        # Create menu
        menu_1 = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label='File', menu=menu_1)
        menu_1.add_command(label="Guess the Number", command=self.guess_game)
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
        btn_guess = Button(self.window, text="Guess the Number", fg="Black", command=self.guess_game)
        btn_close = Button(self.window, text='Close', fg="Black", command=self.closeProgram)

        # Set buttons to grid
        btn_guess.grid(column=1, row=1)
        btn_close.grid(column=1, row=2)

        # Align to center
        self.window.columnconfigure(0, weight=1)
        self.window.columnconfigure(1, weight=1)
        self.window.columnconfigure(2, weight=1)

    #Buttons 
    def closeProgram(self):
        self.window.quit()

    def show_about(self):
        about_message = \
        "This is a test of the About Section \
        \n so now I will keep testing \
        \n This is version 0.0.01 \
        \n Not sure what it will be, likely a multi game thing"
        NewWindow(self.window, "About", self.menu_bar, about_message)

    def show_documentation(self):
        doc_message = "This is a test of the Documentation Section \
                        \n It is just a test of Python stuff"
        NewWindow(self.window, "Documentation", self.menu_bar, doc_message)    

    def guess_game(self):
        game_msg = "Test Message"
        GuessingGame(self.window, "Guess the Number", self.menu_bar, game_msg)

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
