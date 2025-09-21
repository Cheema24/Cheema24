import random
import tkinter as tk
from tkinter import messagebox

def roll_dice():
    return random.randint(1, 6)

def player_timer():
    global player_time_left
    if player_time_left > 0:
        player_time_left -= 1
        player_timer_label.config(text=f"Time left: {player_time_left}s")
        root.after(1000, player_timer)
    else:
        play_game()

def cpu_timer():
    global cpu_time_left
    if cpu_time_left > 0:
        cpu_time_left -= 1
        cpu_timer_label.config(text=f"Time left: {cpu_time_left}s")
        root.after(1000, cpu_timer)
    else:
        play_game()

def play_game():
    global player_money, cpu_money, player_time_left, cpu_time_left
    bet = int(bet_entry.get())
    if bet == 0:
        messagebox.showinfo("Game Over", f"Thanks for playing! Your final balance is £{player_money}\nCPU's final balance is £{cpu_money}")
        root.destroy()
        return
    if bet > player_money:
        messagebox.showwarning("Invalid Bet", "You don't have enough money to place that bet.")
        return

    # Player's turn
    dice1 = roll_dice()
    dice2 = roll_dice()
    player_dice1_label.config(text=dice_faces[dice1])
    player_dice2_label.config(text=dice_faces[dice2])
    total = dice1 + dice2
    if total == 7:
        player_money += bet
        result_label.config(text=f"You rolled a {dice1} and a {dice2}. Congratulations! You won £{bet}", fg="gold")
    else:
        player_money -= bet
        result_label.config(text=f"You rolled a {dice1} and a {dice2}. Sorry, you lost £{bet}", fg="red")
    player_balance_label.config(text=f"Your current balance is £{player_money}")

    if player_money <= 0:
        messagebox.showinfo("Game Over", "Sorry, you're out of money! Game over.")
        root.destroy()
        return

    # CPU's turn after 7 seconds
    root.after(7000, cpu_turn)

def cpu_turn():
    global cpu_money
    cpu_bet = min(cpu_money, random.randint(1, 10))
    dice1 = roll_dice()
    dice2 = roll_dice()
    cpu_dice1_label.config(text=dice_faces[dice1])
    cpu_dice2_label.config(text=dice_faces[dice2])
    total = dice1 + dice2
    if total == 7:
        cpu_money += cpu_bet
        cpu_result_label.config(text=f"CPU rolled a {dice1} and a {dice2}. CPU won £{cpu_bet}", fg="gold")
    else:
        cpu_money -= cpu_bet
        cpu_result_label.config(text=f"CPU rolled a {dice1} and a {dice2}. CPU lost £{cpu_bet}", fg="red")
    cpu_balance_label.config(text=f"CPU's current balance is £{cpu_money}")

    if cpu_money <= 0:
        messagebox.showinfo("Game Over", "CPU is out of money! You win the game.")
        root.destroy()

# Initialize game
player_money = 100
cpu_money = 100
player_time_left = 7
cpu_time_left = 7

# Dice faces using Unicode characters
dice_faces = {
    1: "\u2680",  # ⚀
    2: "\u2681",  # ⚁
    3: "\u2682",  # ⚂
    4: "\u2683",  # ⚃
    5: "\u2684",  # ⚄
    6: "\u2685"   # ⚅
}

# Create the main window
root = tk.Tk()
root.title("Lucky Seven")
root.geometry("600x400")  # Set the window size to 600x400 pixels
root.configure(bg="darkgreen")  # Set background color

# Create and place widgets
tk.Label(root, text="Welcome to Lucky Seven!", font=("Helvetica", 20, "bold"), bg="darkgreen", fg="gold").pack(pady=20, expand=True, fill='both')
player_balance_label = tk.Label(root, text=f"Your current balance is £{player_money}", font=("Helvetica", 14), bg="darkgreen", fg="white")
player_balance_label.pack(expand=True, fill='both')
cpu_balance_label = tk.Label(root, text=f"CPU's current balance is £{cpu_money}", font=("Helvetica", 14), bg="darkgreen", fg="white")
cpu_balance_label.pack(expand=True, fill='both')

tk.Label(root, text="Place your bet (enter 0 to quit):", font=("Helvetica", 14), bg="darkgreen", fg="white").pack(pady=10, expand=True, fill='both')
bet_entry = tk.Entry(root, font=("Helvetica", 14), width=10)  # Set the width of the entry box to 10
bet_entry.pack(pady=5)

result_label = tk.Label(root, text="", font=("Helvetica", 14), bg="darkgreen")
result_label.pack(pady=10, expand=True, fill='both')
cpu_result_label = tk.Label(root, text="", font=("Helvetica", 14), bg="darkgreen")
cpu_result_label.pack(pady=10, expand=True, fill='both')

# Create frames for player and CPU dice
player_frame = tk.Frame(root, bg="darkgreen")
player_frame.pack(side="right", padx=20, pady=10, expand=True, fill='both')
cpu_frame = tk.Frame(root, bg="darkgreen")
cpu_frame.pack(side="left", padx=20, pady=10, expand=True, fill='both')

player_dice1_label = tk.Label(player_frame, text="", font=("Helvetica", 50), bg="darkgreen", fg="white")
player_dice1_label.pack(pady=5, expand=True, fill='both')
player_dice2_label = tk.Label(player_frame, text="", font=("Helvetica", 50), bg="darkgreen", fg="white")
player_dice2_label.pack(pady=5, expand=True, fill='both')

cpu_dice1_label = tk.Label(cpu_frame, text="", font=("Helvetica", 50), bg="darkgreen", fg="white")
cpu_dice1_label.pack(pady=5, expand=True, fill='both')
cpu_dice2_label = tk.Label(cpu_frame, text="", font=("Helvetica", 50), bg="darkgreen", fg="white")
cpu_dice2_label.pack(pady=5, expand=True, fill='both')

player_timer_label = tk.Label(root, text=f"Time left: {player_time_left}s", font=("Helvetica", 14), bg="darkgreen", fg="white")
player_timer_label.pack(pady=5, expand=True, fill='both')
cpu_timer_label = tk.Label(root, text=f"Time left: {cpu_time_left}s", font=("Helvetica", 14), bg="darkgreen", fg="white")
cpu_timer_label.pack(pady=5, expand=True, fill='both')

bet_button = tk.Button(root, text="Roll Dice", command=player_timer, font=("Helvetica", 14), bg="gold", fg="black")
bet_button.pack(pady=20, expand=True, fill='both')

# Start the main event loop
root.mainloop()