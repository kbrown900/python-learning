import random
from tkinter import *
from tkinter import messagebox

class HangmanGame:
    def __init__(self, parent_window, title, menu_bar):
        self.new_window = Toplevel(parent_window)
        self.new_window.title(title)
        self.new_window.geometry('400x300')
        self.new_window.iconbitmap("resources/images/Support_Icon.ico")
        self.new_window.config(menu=menu_bar)

        self.word_list = [
            "PYTHON", "DEVELOPER", "PROGRAM", "HANGMAN", "CODING", "COMPUTER", "SOFTWARE",
            "LAPTOP", "MONITOR", "KEYBOARD", "MOUSE", "PRINTER", "INTERNET", "GITHUB", "FIREWALL",
            "SECURITY", "VIRTUAL", "BINARY", "VARIABLE", "FUNCTION", "DATABASE", "ALGORITHM",
            "NETWORK", "STORAGE", "ENCRYPTION", "PROCESSOR", "HARDWARE", "GRAPHICS", "GAMING",
            "DESKTOP", "WIRELESS", "SERVER", "BROWSER", "SEARCH", "DISPLAY", "CONNECTION",
            "PASSWORD", "BACKUP", "HACKER", "ROUTER", "FIRMWARE", "MALWARE", "CLOUD",
            "OPERATING", "COMMAND", "TERMINAL", "SYSTEM", "DEBUGGING", "COMPILER", "LOOP",
            "CONSOLE", "VARIABLE", "PYTHONIC", "BOOLEAN", "INTEGER", "STRING", "LIBRARY",
            "FRAMEWORK", "RECURSION", "INSTANCE", "CONSTRUCTOR", "METHOD", "ATTRIBUTE",
            "ARGUMENT", "STATEMENT", "EXCEPTION", "INDEX", "SYNTAX", "QUERY", "SCALABILITY",
            "DATASTRUCTURE", "MEMORY", "EXECUTION", "CACHE", "ITERATOR", "STATEMENT",
            "OPTIMIZATION", "PARADIGM", "THREADING", "RESPONSE", "SESSION", "TOKEN",
            "INHERITANCE", "ENCAPSULATION", "POLYMORPHISM", "ABSTRACTION"
            ]
        self.secret_word = random.choice(self.word_list)
        self.guessed_word = ["_"] * len(self.secret_word)
        self.attempts = 6
        self.guessed_letters = set()

        self.setup_ui()

    def setup_ui(self):
        # Display the word with underscores
        self.word_label = Label(self.new_window, text=" ".join(self.guessed_word))
        self.word_label.pack(pady=10)

        # Attempts left
        self.attempts_label = Label(self.new_window, text=f"Attempts Left: {self.attempts}")
        self.attempts_label.pack(pady=5)

        # Entry for letter guesses
        self.entry_label = Label(self.new_window, text="Enter a letter:")
        self.entry_label.pack()

        self.letter_entry = Entry(self.new_window, width=5)
        self.letter_entry.pack()
        self.letter_entry.bind("<Return>", self.check_guess)

        # Submit button
        self.submit_button = Button(self.new_window, text="Submit Guess", command=self.check_guess)
        self.submit_button.pack(pady=5)

        # Message Label
        self.message_label = Label(self.new_window, text="", fg="red")
        self.message_label.pack()

        # Close Button
        close_button = Button(self.new_window, text="Close", command=self.new_window.destroy)
        close_button.pack(pady=10)

    def check_guess(self, event=None):
        guess = self.letter_entry.get().upper()
        self.letter_entry.delete(0, END)

        if len(guess) != 1 or not guess.isalpha():
            self.message_label.config(text="Please enter a single letter.")
            return

        if guess in self.guessed_letters:
            self.message_label.config(text="You already guessed that letter!")
            return

        self.guessed_letters.add(guess)

        if guess in self.secret_word:
            for i, letter in enumerate(self.secret_word):
                if letter == guess:
                    self.guessed_word[i] = guess
        else:
            self.attempts -= 1

        self.update_display()

        if "_" not in self.guessed_word:
            messagebox.showinfo("Congratulations!", "You guessed the word!")
            self.new_window.destroy()
        elif self.attempts == 0:
            messagebox.showinfo("Game Over", f"You lost! The word was {self.secret_word}.")
            self.new_window.destroy()

    def update_display(self):
        self.word_label.config(text=" ".join(self.guessed_word))
        self.attempts_label.config(text=f"Attempts Left: {self.attempts}")
        self.message_label.config(text="")

