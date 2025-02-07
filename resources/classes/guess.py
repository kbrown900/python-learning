import random
from tkinter import *
from tkinter import messagebox

class GuessingGame:
    def __init__(self, parent_window, title, menu_bar, message):
        self.new_window = Toplevel(parent_window)
        self.new_window.title(title)
        self.new_window.geometry('350x200')
        self.new_window.iconbitmap("resources/images/Support_Icon.ico")
        self.new_window.config(menu=menu_bar)
        self.secret_number = random.randint(1, 100)
        self.attempts = 0

        self.label = Label(self.new_window, text="Guess a number between 1 and 100:")
        self.label.pack(pady=10)

        # Entry Validation
        validatecmd = self.new_window.register(self.validate_input)
        self.entry = Entry(self.new_window, validate="key", validatecommand=(validatecmd, '%P'))
        self.entry.pack(pady=5)
        self.entry.bind("<Return>", self.check_guess)

        self.button = Button(self.new_window, text="Submit Guess", command=self.check_guess)
        self.button.pack(pady=5)
        
        self.button2 = Button(self.new_window, text="Reset", command=self.reset_game)
        self.button2.pack(pady=5)

        self.button3 = Button(self.new_window, text="Close", command=self.new_window.destroy)
        self.button3.pack(pady=5)

        self.result_label = Label(self.new_window, text="")
        self.result_label.pack(pady=10)        

    def check_guess(self, event=None):
        try:
            guess = int(self.entry.get())
            self.attempts += 1

            if guess < self.secret_number:
                self.result_label.config(text="Too low! Try again.", fg="red")
            elif guess > self.secret_number:
                self.result_label.config(text="Too high! Try again.", fg="red")
            else:
                messagebox.showinfo("Congratulations!", f"You guessed the number in {self.attempts} attempts!")
                self.reset_game()
                self.new_window.destroy()
        except ValueError:
            self.result_label.config(text="Please enter a valid number.", fg="red")

    def validate_input(self, new_value):
        if new_value.isdigit() or new_value == "":
          return True
        return False

    def reset_game(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.entry.delete(0, END)
        self.result_label.config(text="")