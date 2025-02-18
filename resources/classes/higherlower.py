import random
from tkinter import *
from tkinter import messagebox
from resources.classes.resources import resource_path

class higherlower:
    def __init__(self, title, menu_bar, parent_window):
        self.new_window = Toplevel(parent_window)
        self.new_window.title(title)
        self.new_window.config(menu=menu_bar)
        self.new_window.geometry("350x200")
        self.new_window.iconbitmap(resource_path("resources/images/Support_Icon.ico"))
        
        self.current_number = random.randint(1, 100)
        self.score = 0
        
        self.label = Label(self.new_window, text=f"Current Number: {self.current_number}")
        self.label.pack(pady=10)
        
        self.higher_button = Button(self.new_window, text="Higher", command=lambda: self.check_guess("higher"))
        self.higher_button.pack(pady=5)
        
        self.lower_button = Button(self.new_window, text="Lower", command=lambda: self.check_guess("lower"))
        self.lower_button.pack(pady=5)
        
        self.score_label = Label(self.new_window, text=f"Score: {self.score}", font=("Arial", 12))
        self.score_label.pack(pady=10)
        
    def check_guess(self, guess):
        next_number = random.randint(1, 100)
        correct_guess = (guess == "higher" and next_number > self.current_number) or \
                        (guess == "lower" and next_number < self.current_number)
        
        if correct_guess:
            self.score += 1
            self.current_number = next_number
            self.label.config(text=f"Current Number: {self.current_number}")
            self.score_label.config(text=f"Score: {self.score}")
        else:
            messagebox.showinfo("Game Over", f"Wrong guess! The final number was {next_number}. Your final score is {self.score}")
            self.new_window.destroy()