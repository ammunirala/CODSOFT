import tkinter as tk
from tkinter import messagebox
import random

def get_computer_choice():
    """Randomly select rock, paper, or scissors for the computer."""
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on user and computer choices."""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game(user_choice):
    global user_score, computer_score
    computer_choice = get_computer_choice()

    result = determine_winner(user_choice, computer_choice)
    if "You win" in result:
        user_score += 1
    elif "Computer wins" in result:
        computer_score += 1

    result_label.config(text=f"You chose: {user_choice}\nComputer chose: {computer_choice}\n{result}")
    score_label.config(text=f"Scores - You: {user_score}, Computer: {computer_score}")

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    result_label.config(text="")
    score_label.config(text=f"Scores - You: {user_score}, Computer: {computer_score}")

# Initialize the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("300x400")
root.configure(bg="#f0f0f0")

user_score = 0
computer_score = 0

# Create and place labels and buttons
title_label = tk.Label(root, text="Rock-Paper-Scissors", font=('Helvetica', 16, 'bold'), bg="#f0f0f0")
title_label.pack(pady=10)

frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(pady=20)

rock_button = tk.Button(frame, text="Rock", width=15, bg="#ff9999", command=lambda: play_game('rock'))
rock_button.grid(row=0, column=0, padx=5, pady=5)

paper_button = tk.Button(frame, text="Paper", width=15, bg="#99ff99", command=lambda: play_game('paper'))
paper_button.grid(row=0, column=1, padx=5, pady=5)

scissors_button = tk.Button(frame, text="Scissors", width=15, bg="#9999ff", command=lambda: play_game('scissors'))
scissors_button.grid(row=0, column=2, padx=5, pady=5)

result_label = tk.Label(root, text="", font=('Helvetica', 12), bg="#f0f0f0")
result_label.pack(pady=20)

score_label = tk.Label(root, text=f"Scores - You: {user_score}, Computer: {computer_score}", font=('Helvetica', 12), bg="#f0f0f0")
score_label.pack(pady=5)

reset_button = tk.Button(root, text="Reset Game", bg="#ffcc99", command=reset_game)
reset_button.pack(pady=10)

# Start the main loop
root.mainloop()