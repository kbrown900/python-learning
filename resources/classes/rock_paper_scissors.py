import random
from tkinter import *
from tkinter import messagebox

class RockPaperScissors:
    def __init__(self, parent_window, title, menu_bar):
        self.new_window = Toplevel(parent_window)
        self.new_window.title(title)
        self.new_window.config(menu=menu_bar)
        self.new_window.geometry('400x300')
        self.new_window.iconbitmap("resources/images/Support_Icon.ico")

        # Label
        self.label = Label(self.new_window, text="Choose Rock, Paper, or Scissors!", font=("Arial", 12))
        self.label.pack(pady=10)

        # Buttons for User Choice
        self.btn_rock = Button(self.new_window, text="Rock", width=15, command=lambda: self.play_game("Rock"))
        self.btn_paper = Button(self.new_window, text="Paper", width=15, command=lambda: self.play_game("Paper"))
        self.btn_scissors = Button(self.new_window, text="Scissors", width=15, command=lambda: self.play_game("Scissors"))

        self.btn_rock.pack(pady=5)
        self.btn_paper.pack(pady=5)
        self.btn_scissors.pack(pady=5)

        # Label to Show Result
        self.result_label = Label(self.new_window, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)

        # Close Button
        self.btn_close = Button(self.new_window, text="Close", width=15, command=self.new_window.destroy)
        self.btn_close.pack(pady=10)

    def play_game(self, user_choice):
        choices = ["Rock", "Paper", "Scissors"]
        computer_choice = random.choice(choices)

        result = ""
        if user_choice == computer_choice:
            result = f"Both chose {user_choice}. It's a tie!"
        elif (user_choice == "Rock" and computer_choice == "Scissors") or \
             (user_choice == "Scissors" and computer_choice == "Paper") or \
             (user_choice == "Paper" and computer_choice == "Rock"):
            result = f"You chose {user_choice}, Computer chose {computer_choice}. You win!"
        else:
            result = f"You chose {user_choice}, Computer chose {computer_choice}. You lose!"

        self.result_label.config(text=result)