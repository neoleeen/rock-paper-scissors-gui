import random
import tkinter as tk


player_score = 0
computer_score = 0
tie_score = 0


def play(player_choice: str) -> None: 
    global player_score, computer_score, tie_score

    computer_choice = random.choice(("rock", "paper", "scissors"))

    if player_choice == computer_choice:
        tie_score += 1
        result = f"It's a tie! You both chose {player_choice}."
    elif (player_choice, computer_choice) in {
        ("rock", "scissors"),
        ("paper", "rock"),
        ("scissors", "paper"),
    }:
        player_score += 1
        result = f"You win! {player_choice.title()} beats {computer_choice}."
    else:
        computer_score += 1
        result = f"You lose! {computer_choice.title()} beats {player_choice}."

    result_label.config(text=result)
    player_score_label.config(text=f"Player wins: {player_score}")
    computer_score_label.config(text=f"Computer wins: {computer_score}")
    tie_score_label.config(text=f"Ties: {tie_score}")


root = tk.Tk()
root.title("Rock Paper Scissors")
root.resizable(False, False)
root.configure(bg="#FFFDF5")

paper = tk.Canvas(root, width=420, height=330, bg="#FFFDF5", highlightthickness=0)
paper.pack()

for y in range(42, 330, 28):
    paper.create_line(0, y, 420, y, fill="#C9DDF0", width=1)
paper.create_line(42, 0, 42, 330, fill="#E7A5A5", width=2)

content = tk.Frame(paper, bg="#FFFDF5")
paper.create_window(58, 12, window=content, anchor=tk.NW, width=345)

tk.Label(
    content,
    text="ROCK  •  PAPER  •  SCISSORS",
    font=("Arial", 16, "bold"),
    bg="#FFFDF5",
    fg="#234F7E",
).pack(pady=(10, 4))

tk.Label(
    content,
    text="Choose your move:",
    font=("Arial", 12),
    bg="#FFFDF5",
    fg="#234F7E",
).pack(pady=(2, 8))

button_frame = tk.Frame(content, bg="#FFFDF5")
button_frame.pack()
for choice in ("rock", "paper", "scissors"):
    tk.Button(
        button_frame,
        text=choice.title(),
        width=10,
        font=("Arial", 10, "bold"),
        bg="#E8F1FA",
        fg="#234F7E",
        activebackground="#D3E5F5",
        activeforeground="#173A5E",
        relief=tk.GROOVE,
        bd=2,
        command=lambda move=choice: play(move),
    ).pack(side=tk.LEFT, padx=4)

result_label = tk.Label(
    content,
    text="The first to score wins the round.",
    font=("Arial", 10),
    bg="#FFFDF5",
    fg="#234F7E",
)
result_label.pack(pady=14)

scoreboard_frame = tk.LabelFrame(
    content,
    text="Scoreboard",
    padx=12,
    pady=8,
    font=("Arial", 10, "bold"),
    bg="#FFFDF5",
    fg="#234F7E",
    relief=tk.SOLID,
    bd=1,
)
scoreboard_frame.pack(padx=12, pady=(0, 12), fill=tk.X)

player_score_label = tk.Label(
    scoreboard_frame, text="Player wins: 0", bg="#FFFDF5", fg="#234F7E"
)
player_score_label.pack(anchor=tk.W)

computer_score_label = tk.Label(
    scoreboard_frame, text="Computer wins: 0", bg="#FFFDF5", fg="#234F7E"
)
computer_score_label.pack(anchor=tk.W)

tie_score_label = tk.Label(
    scoreboard_frame, text="Ties: 0", bg="#FFFDF5", fg="#234F7E"
)
tie_score_label.pack(anchor=tk.W)

root.mainloop()
