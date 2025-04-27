import tkinter as tk
from tkinter import messagebox
import random

class NumberGuessingGameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🎯 Number Guessing Game")
        self.root.geometry("500x400")
        self.root.config(bg="#f0f8ff")
        self.root.resizable(False, False)

        self.header_font = ("Comic Sans MS", 20, "bold")
        self.label_font = ("Arial", 12)
        self.button_font = ("Arial", 10, "bold")

        self.setup_difficulty_screen()

    def setup_difficulty_screen(self):
        self.clear_screen()

        frame = tk.Frame(self.root, bg="#f0f8ff")
        frame.pack(expand=True)

        tk.Label(frame, text="🎯 Choose Difficulty", font=self.header_font, bg="#f0f8ff", fg="#003366").pack(pady=20)

        tk.Button(frame, text="Easy (1-50)", font=self.button_font, bg="#ccffcc", fg="black",
                  command=lambda: self.start_game(1, 50, 10)).pack(pady=8, ipadx=10)

        tk.Button(frame, text="Medium (1-100)", font=self.button_font, bg="#ffffcc", fg="black",
                  command=lambda: self.start_game(1, 100, 7)).pack(pady=8, ipadx=10)

        tk.Button(frame, text="Hard (1-200)", font=self.button_font, bg="#ffcccc", fg="black",
                  command=lambda: self.start_game(1, 200, 5)).pack(pady=8, ipadx=10)

    def start_game(self, low, high, max_attempts):
        self.low = low
        self.high = high
        self.max_attempts = max_attempts
        self.attempts = 0
        self.number_to_guess = random.randint(low, high)

        self.clear_screen()

        frame = tk.Frame(self.root, bg="#f0f8ff")
        frame.pack(expand=True)

        tk.Label(frame, text=f"Guess a number between {low} and {high}", font=self.label_font,
                 bg="#f0f8ff", fg="#003366").pack(pady=10)

        self.entry = tk.Entry(frame, font=("Arial", 14), width=10, justify="center")
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", lambda event: self.check_guess())

        self.feedback_label = tk.Label(frame, text="", font=self.label_font, bg="#f0f8ff", fg="#cc0000")
        self.feedback_label.pack(pady=5)

        self.attempts_label = tk.Label(frame, text=f"Attempts: {self.attempts}/{self.max_attempts}",
                                       font=self.label_font, bg="#f0f8ff", fg="#003366")
        self.attempts_label.pack()

        tk.Button(frame, text="🎯 Submit Guess", font=self.button_font, bg="#add8e6", command=self.check_guess).pack(pady=10)

        button_frame = tk.Frame(frame, bg="#f0f8ff")
        button_frame.pack(pady=20)

        tk.Button(button_frame, text="🔁 Restart", font=self.button_font, bg="#d9ead3", width=10,
                  command=self.setup_difficulty_screen).pack(side="left", padx=20)
        tk.Button(button_frame, text="❌ Exit", font=self.button_font, bg="#f4cccc", width=10,
                  command=self.root.quit).pack(side="right", padx=20)

    def check_guess(self):
        guess = self.entry.get()
        if not guess.isdigit():
            self.feedback_label.config(text="❗ Please enter a valid number.")
            return

        guess = int(guess)
        self.attempts += 1
        self.attempts_label.config(text=f"Attempts: {self.attempts}/{self.max_attempts}")

        if guess < self.number_to_guess:
            self.feedback_label.config(text="🔻 Too low!")
        elif guess > self.number_to_guess:
            self.feedback_label.config(text="🔺 Too high!")
        else:
            messagebox.showinfo("🎉 Congratulations!", f"You guessed it in {self.attempts} attempts!")
            self.setup_difficulty_screen()
            return

        if self.attempts >= self.max_attempts:
            messagebox.showinfo("💥 Game Over", f"Out of attempts! The number was {self.number_to_guess}.")
            self.setup_difficulty_screen()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

# Launch the GUI game
root = tk.Tk()
game = NumberGuessingGameGUI(root)
root.mainloop()
