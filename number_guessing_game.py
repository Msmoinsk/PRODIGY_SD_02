import tkinter as tk
from tkinter import messagebox
import random
from tkinter import ttk

class GuessingGame(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Guess the Number!")
        self.geometry("500x500")
        self.configure(bg="#E0F7F8")

        self.random_number = None
        self.attempts = 0
        self.max_attempts = 10

        self.create_widgets()
        self.reset_game()

    def create_widgets(self):
        # Title
        self.title_label = tk.Label(self, text="Guess the Number!", font=("Helvetica", 28, "bold"), fg="#00796B", bg="#E0F7F8")
        self.title_label.pack(pady=20)

        # Instruction Label
        self.instruction_label = tk.Label(self, text="Guess a number between 1 and 100:", font=("Arial", 16), bg="#E0F7F8")
        self.instruction_label.pack(pady=10)

        # Entry Field
        self.guess_field = tk.Entry(self, font=("Arial", 16), borderwidth=2, relief="solid", width=15)
        self.guess_field.pack(pady=10)

        # Guess Button
        self.guess_button = tk.Button(self, text="Guess", font=("Arial", 16, "bold"), command=self.handle_guess, bg="#4CAF50", fg="white", relief="flat", width=12)
        self.guess_button.pack(pady=10)

        # Reset Button
        self.reset_button = tk.Button(self, text="Reset", font=("Arial", 16, "bold"), command=self.reset_game, bg="#F44336", fg="white", relief="flat", width=12)
        self.reset_button.pack(pady=15)

        # Feedback Label
        self.feedback_label = tk.Label(self, text="", font=("Arial", 14), bg="#E0F7F8")
        self.feedback_label.pack(pady=15)

        # Attempts Label
        self.attempts_label = tk.Label(self, text=f"Attempts left: {self.max_attempts}", font=("Arial", 14), bg="#E0F7F8")
        self.attempts_label.pack(pady=10)

        # Progress Bar
        self.progress_bar = ttk.Progressbar(self, orient="horizontal", length=300, mode="determinate", maximum=self.max_attempts)
        self.progress_bar.pack(pady=10)
        self.progress_bar["value"] = self.max_attempts

    def reset_game(self):
        self.random_number = random.randint(1, 100)
        self.attempts = 0
        self.guess_field.delete(0, tk.END)
        self.feedback_label.config(text="")
        self.attempts_label.config(text=f"Attempts left: {self.max_attempts}")
        self.progress_bar["value"] = self.max_attempts

    def handle_guess(self):
        guess_text = self.guess_field.get()
        if not guess_text:
            messagebox.showerror("Invalid Input", "Please enter a number.")
            return

        try:
            guess = int(guess_text)
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")
            return

        if guess < 1 or guess > 100:
            messagebox.showerror("Invalid Input", "Please enter a number between 1 and 100.")
            return

        self.attempts += 1
        attempts_left = self.max_attempts - self.attempts
        self.progress_bar["value"] = attempts_left

        if guess < self.random_number:
            self.feedback_label.config(text=f"{guess} is too low!", fg="blue")
        elif guess > self.random_number:
            self.feedback_label.config(text=f"{guess} is too high!", fg="red")
        else:
            self.feedback_label.config(text=f"Congratulations! {guess} is correct!", fg="#00796B")
            messagebox.showinfo("You Win!", f"You guessed the number in {self.attempts} attempts!")
            return

        self.attempts_label.config(text=f"Attempts left: {attempts_left}")

        if attempts_left <= 0:
            self.feedback_label.config(text=f"Game Over! The number was: {self.random_number}", fg="red")
            messagebox.showinfo("Game Over", f"Game Over! The number was: {self.random_number}")

if __name__ == "__main__":
    app = GuessingGame()
    app.mainloop()
