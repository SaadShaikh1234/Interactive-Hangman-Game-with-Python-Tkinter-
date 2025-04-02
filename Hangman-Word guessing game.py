import random
import tkinter as tk
from tkinter import messagebox
import os

# Word categories with hints for Single Player mode
word_categories = {
    "Tech": [("python", "Popular programming language"),
             ("algorithm", "Set of steps to solve a problem"),
             ("database", "Stores structured data")],
    "Sports": [("cricket", "A game played with bat and ball"),
               ("football", "Most popular sport worldwide"),
               ("tennis", "Played with a racket and ball")],
    "Movies": [("avatar", "Highest-grossing sci-fi movie"),
               ("titanic", "Famous 1997 romantic movie"),
               ("joker", "A DC villain got his own movie")],
    "Animals": [("elephant", "Largest land animal"),
                ("giraffe", "Tallest animal in the world"),
                ("penguin", "A bird that cannot fly")],
}

# ASCII art for hangman stages
hangman_pics = [
    """
       ------
       |    |
       |
       |
       |
       |
    -------
    """,
    """
       ------
       |    |
       |    O
       |
       |
       |
    -------
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    -------
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    -------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    -------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    -------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    -------
    GAME OVER!
    """
]

# Leaderboard file
LEADERBOARD_FILE = "leaderboard.txt"


class HangmanApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        self.root.geometry("600x400")
        self.root.configure(bg="#add8e6")  # Light blue background

        # Game State Variables
        self.word = ""
        self.hint = ""
        self.guessed_letters = set()
        self.attempts = 0
        self.player_name = ""

        # Navigation Frames
        self.frame1 = None
        self.frame2 = None
        self.frame3 = None

        # Build Page 1 (Welcome Screen)
        self.build_page1()
        self.create_menu()

    def create_menu(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New Game", command=self.build_page1)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)

        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.show_about)
        help_menu.add_command(label="Leaderboard", command=self.show_leaderboard)

    def show_about(self):
        messagebox.showinfo("About Hangman", "Hangman Game\nVersion 1.0\nCreated by [Your Name]")

    def build_page1(self):
        """Build the welcome screen with mode selection."""
        self.reset_frames()

        self.frame1 = tk.Frame(self.root, bg="#add8e6")
        self.frame1.pack(fill="both", expand=True)

        # Add title
        title = tk.Label(self.frame1, text="Welcome to Hangman!", font=("Arial", 28), bg="#add8e6", fg="#ffffff")
        title.pack(pady=40)

        # Add buttons for Single Player and Multiplayer modes
        single_player_btn = tk.Button(self.frame1, text="Single Player", font=("Arial", 16), bg="#ffffff", fg="#000000",
                                      command=self.build_singleplayer_page2, width=20)
        single_player_btn.pack(pady=20)

        multiplayer_btn = tk.Button(self.frame1, text="Multiplayer", font=("Arial", 16), bg="#ffffff", fg="#000000",
                                     command=self.build_multiplayer_page2, width=20)
        multiplayer_btn.pack(pady=10)

    def build_singleplayer_page2(self):
        """Build the Single Player setup screen."""
        self.reset_frames()

        self.frame2 = tk.Frame(self.root, bg="#eaf2f8")
        self.frame2.pack(fill="both", expand=True)

        # Title
        tk.Label(self.frame2, text="Single Player Mode", font=("Arial", 24), bg="#eaf2f8", fg="#333333").pack(pady=20)

        # Category selection
        tk.Label(self.frame2, text="Choose a Category:", font=("Arial", 16), bg="#eaf2f8", fg="#333333").pack(pady=5)
        self.category_var = tk.StringVar(value="Tech")
        category_menu = tk.OptionMenu(self.frame2, self.category_var, *word_categories.keys())
        category_menu.config(font=("Arial", 14), bg="#ffffff", fg="#333333")
        category_menu.pack(pady=5)

        # Player name input
        tk.Label(self.frame2, text="Enter Your Name:", font=("Arial", 16), bg="#eaf2f8", fg="#333333").pack(pady=5)
        self.name_entry = tk.Entry(self.frame2, font=("Arial", 14), bg="#ffffff", fg="#333333")
        self.name_entry.pack(pady=10)

        # Start Game button
        tk.Button(self.frame2, text="Play", font=("Arial", 16), bg="#008080", fg="#ffffff",
                  command=self.start_singleplayer_game).pack(pady=20)

    def build_multiplayer_page2(self):
        """Build the Multiplayer setup screen."""
        self.reset_frames()

        self.frame2 = tk.Frame(self.root, bg="#eaf2f8")
        self.frame2.pack(fill="both", expand=True)

        # Title
        tk.Label(self.frame2, text="Multiplayer Mode", font=("Arial", 24), bg="#eaf2f8", fg="#333333").pack(pady=20)

        # Player name input
        tk.Label(self.frame2, text="Player 1 Name:", font=("Arial", 16), bg="#eaf2f8", fg="#333333").pack(pady=5)
        self.player1_name_entry = tk.Entry(self.frame2, font=("Arial", 14), bg="#ffffff", fg="#333333")
        self.player1_name_entry.pack(pady=10)

        # Word input
        tk.Label(self.frame2, text="Player 1: Enter a Word:", font=("Arial", 16), bg="#eaf2f8", fg="#333333").pack(pady=5)
        self.word_entry = tk.Entry(self.frame2, font=("Arial", 14), bg="#ffffff", fg="#333333")
        self.word_entry.pack(pady=10)

        # Hint input
        tk.Label(self.frame2, text="Enter a Hint:", font=("Arial", 16), bg="#eaf2f8", fg="#333333").pack(pady=5)
        self.hint_entry = tk.Entry(self.frame2, font=("Arial", 14), bg="#ffffff", fg="#333333")
        self.hint_entry.pack(pady=10)

        # Start Game button
        tk.Button(self.frame2, text="Play", font=("Arial", 16), bg="#008080", fg="#ffffff",
                  command=self.start_multiplayer_game).pack(pady=20)

    def start_singleplayer_game(self):
        """Start a Single Player game."""
        if not self.name_entry.get():
            messagebox.showerror("Input Error", "Please enter your name.")
            return
        category = self.category_var.get()
        self.player_name = self.name_entry.get()
        self.word, self.hint = random.choice(word_categories[category])
        self.reset_game()
        self.build_page3()

    def start_multiplayer_game(self):
        """Start a Multiplayer game."""
        if not self.word_entry.get() or not self.hint_entry.get() or not self.player1_name_entry.get():
            messagebox.showerror("Input Error", "Please enter a word, hint, and player name.")
            return
        self.player_name = self.player1_name_entry.get()
        self.word = self.word_entry.get().lower()
        self.hint = self.hint_entry.get()
        self.reset_game()
        self.build_page3()

    def reset_game(self):
        """Reset game variables."""
        self.guessed_letters = set()
        self.attempts = 0

    def build_page3(self):
        """Build the gameplay screen."""
        self.reset_frames()

        # Create a frame for the gameplay screen
        self.frame3 = tk.Frame(self.root, bg="#f7f9fc")
        self.frame3.pack(fill="both", expand=True, pady=20)

        # Hangman ASCII Display
        self.hangman_label = tk.Label(self.frame3, text=hangman_pics[0], font=("Courier", 14), justify="left", bg="#f7f9fc", fg="#333333")
        self.hangman_label.pack(pady=10)

        # Attempts Left
        self.attempts_label = tk.Label(self.frame3, text="Attempts Left: 6", font=("Arial", 16), bg="#f7f9fc", fg="#333333")
        self.attempts_label.pack(pady=5)

        # Guessed Word Display
        self.word_label = tk.Label(self.frame3, text=" ".join(["_" for _ in self.word]), font=("Courier", 20), bg="#f7f9fc", fg="#333333")
        self.word_label.pack(pady=10)

        # Hint Display
        self.hint_label = tk.Label(self.frame3, text=f"Hint: {self.hint}", font=("Arial", 16), bg="#f7f9fc", fg="#333333")
        self.hint_label.pack(pady=5)

        # Input Field for Guessing Letters
        self.input_field = tk.Entry(self.frame3, font=("Arial", 14), bg="#ffffff", fg="#333333")
        self.input_field.pack(pady=5)

        # Guess Button
        tk.Button(self.frame3, text="Guess", font=("Arial", 16), bg="#008080", fg="#ffffff",
                  command=self.make_guess).pack(pady=10)

    def make_guess(self):
        """Handle the player's guess."""
        guess = self.input_field.get().lower()
        if len(guess) != 1 or not guess.isalpha():
            messagebox.showerror("Invalid Input", "Please enter a single letter.")
            return

        if guess in self.guessed_letters:
            messagebox.showwarning("Already Guessed", "You already guessed that letter!")
            return

        self.guessed_letters.add(guess)
        self.input_field.delete(0, tk.END)

        if guess in self.word:
            display = " ".join([letter if letter in self.guessed_letters else "_" for letter in self.word])
            self.word_label.config(text=display)
            if set(self.word) <= self.guessed_letters:
                self.update_leaderboard(10)  # Add 10 points for a win
                messagebox.showinfo("Congratulations", f"You guessed the word: {self.word}")
                self.end_game()
        else:
            self.attempts += 1
            self.hangman_label.config(text=hangman_pics[self.attempts])
            self.attempts_label.config(text=f"Attempts Left: {6 - self.attempts}")
            if self.attempts == 6:
                messagebox.showinfo("Game Over", f"You lost! The word was: {self.word}")
                self.end_game()

    def end_game(self):
        """Prompt the user to play again or show the leaderboard."""
        play_again = messagebox.askyesno("Play Again?", "Do you want to play again?")
        if play_again:
            self.build_page1()
        else:
            self.show_leaderboard()

    def show_leaderboard(self):
        """Display the leaderboard."""
        self.reset_frames()
        leaderboard_frame = tk.Frame(self.root, bg="#f4f4f8")
        leaderboard_frame.pack(fill="both", expand=True, pady=20)

        # Add leaderboard title
        tk.Label(leaderboard_frame, text="Leaderboard", font=("Arial", 24), bg="#f4f4f8", fg="#333333").pack(pady=20)

        # Retrieve and display scores
        scores = self.load_leaderboard()
        if scores:
            sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
            for rank, (player, score) in enumerate(sorted_scores, 1):
                tk.Label(leaderboard_frame, text=f"{rank}. {player} - {score} points", font=("Arial", 16), bg="#f4f4f8", fg="#333333").pack(pady=5)
        else:
            tk.Label(leaderboard_frame, text="No scores yet!", font=("Arial", 16), bg="#f4f4f8", fg="#333333").pack(pady=20)

        # Add button to return to the main menu
        tk.Button(leaderboard_frame, text="Back to Main Menu", font=("Arial", 16), bg="#008080", fg="#ffffff",
                  command=lambda: self.redirect_to_main_menu(leaderboard_frame)).pack(pady=20)

    def redirect_to_main_menu(self, frame):
        """Clear the leaderboard content and redirect to the main menu."""
        frame.destroy()  # Destroy the leaderboard frame
        self.build_page1()

    def reset_frames(self):
        """Reset all frames."""
        if self.frame1:
            self.frame1.destroy()
        if self.frame2:
            self.frame2.destroy()
        if self.frame3:
            self.frame3.destroy()

    def update_leaderboard(self, points):
        """Update leaderboard with the player's score."""
        scores = self.load_leaderboard()
        scores[self.player_name] = scores.get(self.player_name, 0) + points
        self.save_leaderboard(scores)

    def save_leaderboard(self, scores):
        """Save scores to the leaderboard file."""
        with open(LEADERBOARD_FILE, "w") as file:
            for name, score in scores.items():
                file.write(f"{name}: {score}\n")

    def load_leaderboard(self):
        """Load scores from the leaderboard file."""
        scores = {}
        if os.path.exists(LEADERBOARD_FILE):
            with open(LEADERBOARD_FILE, "r") as file:
                for line in file:
                    name, score = line.strip().split(": ")
                    scores[name] = int(score)
        return scores

# Run the Application
if __name__ == "__main__":
    root = tk.Tk()
    app = HangmanApp(root)
    root.mainloop()
