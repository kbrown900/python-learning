from tkinter import *
from resources.classes.Windows import NewWindow
from resources.classes.guess import GuessingGame
from resources.classes.rock_paper_scissors import RockPaperScissors

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
        menu_1.add_command(label="Rock Paper Scissors", command=self.rock_paper_scissors)
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
        btn_rps = Button(self.window, text="Rock Paper Scissors", fg="Black", command=self.rock_paper_scissors)
        btn_close = Button(self.window, text='Close', fg="Black", command=self.closeProgram)

        # Set buttons to grid
        btn_guess.grid(column=1, row=1)
        btn_rps.grid(column=1, row=2)
        btn_close.grid(column=1, row=3)

        # Align to center
        self.window.columnconfigure(0, weight=1)
        self.window.columnconfigure(1, weight=1)
        self.window.columnconfigure(2, weight=1)

    #Buttons 
    def closeProgram(self):
        self.window.quit()

    def show_about(self):
        about_message = (
        "About\n"
        "This program is a simple testing of various\n"
        "games that are made in Python.\n"
        "v.0.0.1"
        )
        NewWindow(self.window, "About", self.menu_bar, about_message)

    def show_documentation(self):
        doc_message = (
        "This is a test of the Documentation Section \n"
        "To play a game click the related button or\n"
        "press File and select the game there."
        )
        NewWindow(self.window, "Documentation", self.menu_bar, doc_message)    

    def guess_game(self):
        GuessingGame(self.window, "Guess the Number", self.menu_bar)

    def rock_paper_scissors(self):
        RockPaperScissors(self.window, "Rock Paper Scissors", self.menu_bar)

# Main entry point
if __name__ == "__main__":
    # Create the main window
    root = Tk()
    app = MainApp(root)
    
    # Start the main loop
    root.mainloop()
