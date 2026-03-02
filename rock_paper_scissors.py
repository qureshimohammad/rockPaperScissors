"""
Create a Rock Paper Scissors game where the player inputs their choice
and plays  against a computer that randomly selects its move, 
with the game showing who won each round.
Add a score counter that tracks player and computer wins, 
and allow the game to continue until the player types “quit”.
""" 
import tkinter as tk
from tkinter import ttk
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")
        self.root.geometry("500x500")
        self.root.configure(bg="#f0f0f0")
        
        # Game variables
        self.player_score = 0
        self.computer_score = 0
        self.ties = 0
        self.round_count = 0  # track number of rounds played
        self.choices = ["Rock", "Paper", "Scissors"]
        
        # Title
        title_label = tk.Label(
            self.root,
            text="Rock Paper Scissors",
            font=("Arial", 24, "bold"),
            bg="#f0f0f0",
            fg="#333333"
        )
        title_label.pack(pady=20)
        
        # Score frame
        score_frame = tk.Frame(self.root, bg="#f0f0f0")
        score_frame.pack(pady=10)
        
        self.score_label = tk.Label(
            score_frame,
            text=f"Player: {self.player_score}  |  Ties: {self.ties}  |  Computer: {self.computer_score}",
            font=("Arial", 14),
            bg="#f0f0f0",
            fg="#333"
        )
        self.score_label.pack()
        
        # Choice display frame
        choice_frame = tk.Frame(self.root, bg="#f0f0f0")
        choice_frame.pack(pady=20)
        
        self.player_choice_label = tk.Label(
            choice_frame,
            text="Your Choice: -",
            font=("Arial", 12),
            bg="#f0f0f0",
            fg="#0066cc"
        )
        self.player_choice_label.pack(side=tk.LEFT, padx=20)
        
        self.computer_choice_label = tk.Label(
            choice_frame,
            text="Computer's Choice: -",
            font=("Arial", 12),
            bg="#f0f0f0",
            fg="#cc0000"
        )
        self.computer_choice_label.pack(side=tk.RIGHT, padx=20)
        
        # Result label
        self.result_label = tk.Label(
            self.root,
            text="",
            font=("Arial", 14, "bold"),
            bg="#f0f0f0",
            fg="#009900",
            wraplength=400
        )
        self.result_label.pack(pady=10)
        
        # Detailed scoreboard (history of rounds)
        scoreboard_frame = tk.Frame(self.root, bg="#f0f0f0")
        scoreboard_frame.pack(pady=10, fill=tk.BOTH, expand=True)

        columns = ("round", "player", "computer", "result")
        self.scoreboard = ttk.Treeview(scoreboard_frame, columns=columns, show="headings", height=8)
        self.scoreboard.heading("round", text="Round")
        self.scoreboard.heading("player", text="Player Choice")
        self.scoreboard.heading("computer", text="Computer Choice")
        self.scoreboard.heading("result", text="Outcome")
        self.scoreboard.column("round", width=60, anchor=tk.CENTER)
        self.scoreboard.column("player", width=120, anchor=tk.CENTER)
        self.scoreboard.column("computer", width=120, anchor=tk.CENTER)
        self.scoreboard.column("result", width=100, anchor=tk.CENTER)
        self.scoreboard.pack(fill=tk.BOTH, expand=True)

        # scrollbar for scoreboard
        scrollbar = ttk.Scrollbar(scoreboard_frame, orient=tk.VERTICAL, command=self.scoreboard.yview)
        self.scoreboard.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Buttons frame
        button_frame = tk.Frame(self.root, bg="#f0f0f0")
        button_frame.pack(pady=30)
        
        # Rock button
        rock_button = tk.Button(
            button_frame,
            text="🪨 Rock",
            font=("Arial", 12, "bold"),
            width=12,
            bg="#4CAF50",
            fg="white",
            command=lambda: self.play("Rock")
        )
        rock_button.grid(row=0, column=0, padx=10, pady=10)
        
        # Paper button
        paper_button = tk.Button(
            button_frame,
            text="📄 Paper",
            font=("Arial", 12, "bold"),
            width=12,
            bg="#2196F3",
            fg="white",
            command=lambda: self.play("Paper")
        )
        paper_button.grid(row=0, column=1, padx=10, pady=10)
        
        # Scissors button
        scissors_button = tk.Button(
            button_frame,
            text="✂️ Scissors",
            font=("Arial", 12, "bold"),
            width=12,
            bg="#FF9800",
            fg="white",
            command=lambda: self.play("Scissors")
        )
        scissors_button.grid(row=0, column=2, padx=10, pady=10)
        
        # Reset button
        reset_button = tk.Button(
            self.root,
            text="Reset Score",
            font=("Arial", 10),
            bg="#f44336",
            fg="white",
            command=self.reset_score
        )
        reset_button.pack(pady=10)
    
    def play(self, player_choice):
        # Get computer's random choice
        computer_choice = random.choice(self.choices)
        
        # Update choice labels
        self.player_choice_label.config(text=f"Your Choice: {player_choice}")
        self.computer_choice_label.config(text=f"Computer's Choice: {computer_choice}")
        
        # Determine winner
        result = self.determine_winner(player_choice, computer_choice)
        
        # Update score and result label
        if result == "win":
            self.player_score += 1
            self.result_label.config(
                text=f"✓ You win! {player_choice} beats {computer_choice}",
                fg="#009900"
            )
        elif result == "lose":
            self.computer_score += 1
            self.result_label.config(
                text=f"✗ You lose! {computer_choice} beats {player_choice}",
                fg="#cc0000"
            )
        else:
            self.ties += 1
            self.result_label.config(
                text=f"= It's a tie! Both chose {player_choice}",
                fg="#FF9800"
            )
        
        # Update score label
        self.score_label.config(
            text=f"Player: {self.player_score}  |  Ties: {self.ties}  |  Computer: {self.computer_score}"
        )

        # insert entry into the detailed scoreboard
        self.round_count += 1
        outcome_text = "Tie" if result == "tie" else ("Win" if result == "win" else "Loss")
        self.scoreboard.insert("", "end", values=(
            self.round_count,
            player_choice,
            computer_choice,
            outcome_text
        ))
    
    def determine_winner(self, player, computer):
        if player == computer:
            return "tie"
        
        # Player wins
        if (player == "Rock" and computer == "Scissors") or \
           (player == "Paper" and computer == "Rock") or \
           (player == "Scissors" and computer == "Paper"):
            return "win"
        
        # Computer wins
        return "lose"
    
    def reset_score(self):
        self.player_score = 0
        self.computer_score = 0
        self.ties = 0
        self.round_count = 0
        self.player_choice_label.config(text="Your Choice: -")
        self.computer_choice_label.config(text="Computer's Choice: -")
        self.result_label.config(text="")
        self.score_label.config(
            text=f"Player: {self.player_score}  |  Ties: {self.ties}  |  Computer: {self.computer_score}"
        )
        # clear scoreboard history
        for item in self.scoreboard.get_children():
            self.scoreboard.delete(item)

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()
