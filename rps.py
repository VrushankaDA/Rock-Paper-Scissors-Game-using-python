import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock, Paper, Scissors Game")
        
        self.choices = ["Rock", "Paper", "Scissors"]
        self.user_score = 0
        self.computer_score = 0

        self.create_buttons()
        self.create_score_labels()

    def create_buttons(self):
        self.rock_button = tk.Button(self.root, text="Rock", command=lambda: self.play_game("Rock"))
        self.rock_button.pack(side=tk.LEFT, padx=10)

        self.paper_button = tk.Button(self.root, text="Paper", command=lambda: self.play_game("Paper"))
        self.paper_button.pack(side=tk.LEFT, padx=10)

        self.scissors_button = tk.Button(self.root, text="Scissors", command=lambda: self.play_game("Scissors"))
        self.scissors_button.pack(side=tk.LEFT, padx=10)

        self.play_again_button = tk.Button(self.root, text="Play Again", command=self.play_again)
        self.play_again_button.pack(side=tk.LEFT, padx=10)
        self.play_again_button["state"] = tk.DISABLED  # Initially disable the play again button

    def create_score_labels(self):
        self.user_score_label = tk.Label(self.root, text="Your Score: 0")
        self.user_score_label.pack()

        self.computer_score_label = tk.Label(self.root, text="Computer Score: 0")
        self.computer_score_label.pack()

    def play_game(self, user_choice):
        computer_choice = random.choice(self.choices)

        result = self.determine_winner(user_choice, computer_choice)

        message = f"You chose {user_choice}\nComputer chose {computer_choice}\nResult: {result}"
        messagebox.showinfo("Result", message)

        self.update_scores(result)
        self.update_score_labels()

        self.play_again_button["state"] = tk.NORMAL  # Enable the play again button

    def determine_winner(self, player, computer):
        if player == computer:
            return "It's a tie!"
        elif (
            (player == "Rock" and computer == "Scissors")
            or (player == "Paper" and computer == "Rock")
            or (player == "Scissors" and computer == "Paper")
        ):
            return "You win!"
        else:
            return "Computer wins!"

    def update_scores(self, result):
        if "You win" in result:
            self.user_score += 1
        elif "Computer wins" in result:
            self.computer_score += 1

    def update_score_labels(self):
        self.user_score_label["text"] = f"Your Score: {self.user_score}"
        self.computer_score_label["text"] = f"Computer Score: {self.computer_score}"

    def play_again(self):
        self.play_again_button["state"] = tk.DISABLED  # Disable the play again button
        self.user_score = 0
        self.computer_score = 0
        self.update_score_labels()

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()
