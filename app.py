import customtkinter as ctk
from tkinter import PhotoImage
from PIL import Image, ImageTk  # Import Pillow for image resizing
import random
import time

# Initialize the main application
app = ctk.CTk()
app.title("Rock-Paper-Scissors")
app.geometry("600x400")

# Set the appearance mode and color theme
ctk.set_appearance_mode("light")  # Brighter theme for a lively look
ctk.set_default_color_theme("blue")

# Global variables
player_choice = None
computer_choice = None

# Helper function to resize images
def load_and_resize_image(file_path, width, height):
    img = Image.open(file_path)
    img = img.resize((width, height))  # Resize image
    return ImageTk.PhotoImage(img)

# Home Screen
def home_screen():
    for widget in app.winfo_children():
        widget.destroy()

    # Title
    label = ctk.CTkLabel(app, text="Rock-Paper-Scissors", font=("Arial", 28, "bold"), text_color="#334195")
    label.pack(pady=20)

    # Description
    description = (
        "Welcome to the classic game of Rock-Paper-Scissors!\n"
        "🎮 Test your luck and skills against the computer.\n"
        "Choose wisely: Rock smashes Scissors, Scissors cut Paper, and Paper wraps Rock.\n"
        "Click 'Start Game' below to begin your adventure!"
    )
    desc_label = ctk.CTkLabel(app, text=description, font=("Arial", 16), text_color="#555555", wraplength=500, justify="center")
    desc_label.pack(pady=20)

    # Start Button
    start_button = ctk.CTkButton(app, text="Start Game", command=game_screen, font=("Arial", 18), fg_color="#334195", hover_color="#556dcf", width=150)
    start_button.pack(pady=30)

# Game Screen
def game_screen():
    for widget in app.winfo_children():
        widget.destroy()

    # Title
    label = ctk.CTkLabel(app, text="Choose Your Option", font=("Arial", 20), text_color="#334195")
    label.pack(pady=10)

    # Images for Rock, Paper, Scissors
    rock_img = load_and_resize_image("Rock.png", 100, 100)  # Resize to fit button
    paper_img = load_and_resize_image("Paper.png", 100, 100)
    scissor_img = load_and_resize_image("Scissor.png", 100, 100)

    # Buttons for each choice
    button_frame = ctk.CTkFrame(app, fg_color="#f3f3f3", corner_radius=10)
    button_frame.pack(pady=20)

    rock_button = ctk.CTkButton(button_frame, image=rock_img, fg_color="#fff",text="", width=100, height=100, command=lambda: play_game("Rock"))
    paper_button = ctk.CTkButton(button_frame, image=paper_img, fg_color="#fff", text="", width=100, height=100, command=lambda: play_game("Paper"))
    scissor_button = ctk.CTkButton(button_frame, image=scissor_img, fg_color="#fff", text="", width=100, height=100, command=lambda: play_game("Scissors"))

    rock_button.image = rock_img  # Keep reference to prevent garbage collection
    paper_button.image = paper_img
    scissor_button.image = scissor_img

    # Arrange buttons
    rock_button.grid(row=0, column=0, padx=15, pady=10)
    paper_button.grid(row=0, column=1, padx=15, pady=10)
    scissor_button.grid(row=0, column=2, padx=15, pady=10)

# Game Logic
def play_game(player):
    global player_choice, computer_choice
    player_choice = player
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])

    animate_computer_choice()

    result_label = ctk.CTkLabel(app, text=f"Computer chose {computer_choice}", font=("Arial", 18), text_color="#334195")
    result_label.pack(pady=10)

    result = determine_winner(player_choice, computer_choice)
    result_text = f"You {result}!"
    result_label = ctk.CTkLabel(app, text=result_text, font=("Arial", 18, "bold"), text_color="#e63946" if result == "Lose" else "#4caf50")
    result_label.pack(pady=10)

    # Play Again and Home Buttons
    restart_button = ctk.CTkButton(app, text="Play Again", command=game_screen, font=("Arial", 16), fg_color="#556dcf", hover_color="#788cff", width=120)
    restart_button.pack(pady=5)

    home_button = ctk.CTkButton(app, text="Home", command=home_screen, font=("Arial", 16), fg_color="#556dcf", hover_color="#788cff", width=120)
    home_button.pack(pady=5)

# Animation for Computer's Choice
def animate_computer_choice():
    anim_label = ctk.CTkLabel(app, text="Computer is choosing...", font=("Arial", 16), text_color="#777777")
    anim_label.pack(pady=10)
    app.update()

    for _ in range(5):  # Simple animation
        anim_label.configure(text=random.choice(["Rock...", "Paper...", "Scissors..."]))
        app.update()
        time.sleep(0.3)

    anim_label.destroy()

# Determine the game winner
def determine_winner(player, computer):
    if player == computer:
        return "Tie"
    elif (player == "Rock" and computer == "Scissors") or \
         (player == "Paper" and computer == "Rock") or \
         (player == "Scissors" and computer == "Paper"):
        return "Win"
    else:
        return "Lose"

# Start the application
home_screen()
app.mainloop()
