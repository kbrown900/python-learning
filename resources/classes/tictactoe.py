from tkinter import *
from tkinter import messagebox

class TicTacToe:
    def __init__(self, parent_window, title, menu_bar):
        self.new_window = Toplevel(parent_window)
        self.new_window.title(title)
        self.new_window.geometry('300x250')
        self.new_window.iconbitmap("resources/images/Support_Icon.ico")
        self.new_window.config(menu=menu_bar)

        self.current_player = "X"
        self.board = [""] * 9  # Empty board
        self.buttons = []

        # Create the game board UI
        self.create_board()

        # Reset Button
        self.reset_button = Button(self.new_window, text="Reset Game", command=self.reset_game)
        self.reset_button.pack(pady=10)
        self.close_button = Button(self.new_window, text="Close", command=self.close_game)
        self.close_button.pack(pady=10)

    def create_board(self):
        """Create a 3x3 Tic-Tac-Toe grid using buttons."""
        frame = Frame(self.new_window)
        frame.pack()

        for i in range(9):
            btn = Button(frame, text="", height=2, width=5,command=lambda i=i: self.make_move(i))
            btn.grid(row=i // 3, column=i % 3)
            self.buttons.append(btn)

    def make_move(self, index):
        """Handles the logic for placing X or O."""
        if self.board[index] == "" and not self.check_winner():
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)

            # Check if the move results in a win
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.new_window.destroy()
                self.disable_buttons()
            elif "" not in self.board:  # Check for draw
                messagebox.showinfo("Game Over", "It's a draw!")
                self.new_window.destroy()
                self.disable_buttons()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"  # Switch turns

    def check_winner(self):
        """Check all win conditions."""
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]  # Diagonals
        ]

        for condition in win_conditions:
            a, b, c = condition
            if self.board[a] == self.board[b] == self.board[c] and self.board[a] != "":
                return True  # A player has won

        return False

    def disable_buttons(self):
        """Disable all buttons after the game ends."""
        for btn in self.buttons:
            btn.config(state=DISABLED)

    def reset_game(self):
        """Reset the board for a new game."""
        self.board = [""] * 9
        self.current_player = "X"
        for btn in self.buttons:
            btn.config(text="", state=NORMAL)

    def close_game(self):
        self.new_window.destroy()
