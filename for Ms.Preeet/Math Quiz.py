import tkinter as tk
from tkinter import messagebox
import random

class MathQuiz:
    def __init__(self, root):
        # Set up the main window
        self.root = root
        self.root.title("Math Quiz")
        self.root.geometry("500x500")  # Set fixed window size to 500x500
        self.root.configure(bg="pink")  # Set background color to pink
        
        # Initialize quiz-related variables
        self.score = 0
        self.current_question = 1
        self.difficulty = None
        self.first_attempt = True
        
        # Create the main menu for difficulty selection
        self.create_menu()

    def create_menu(self):
        # Clear any existing widgets
        self.clear_window()
        
        # Display introductory text and difficulty selection buttons
        tk.Label(self.root, text="Hi, this is Cyle of CC level 5! Try my quiz.", font=("Arial", 16), bg="pink").pack(pady=10)
        tk.Label(self.root, text="Select Difficulty Level", font=("Arial", 14), bg="pink").pack(pady=5)
        
        # Difficulty level buttons
        tk.Button(self.root, text="1. Easy", command=lambda: self.start_quiz(1)).pack(pady=5)
        tk.Button(self.root, text="2. Moderate", command=lambda: self.start_quiz(2)).pack(pady=5)
        tk.Button(self.root, text="3. Advanced", command=lambda: self.start_quiz(3)).pack(pady=5)

    def start_quiz(self, difficulty):
        # Set up quiz based on the selected difficulty level
        self.difficulty = difficulty
        self.score = 0
        self.current_question = 1
        self.first_attempt = True
        self.next_question()  # Start the first question

    def random_int(self):
        # Generate a random integer based on difficulty level
        if self.difficulty == 1:
            return random.randint(1, 9)  # Easy: single digits
        elif self.difficulty == 2:
            return random.randint(10, 99)  # Moderate: double digits
        elif self.difficulty == 3:
            return random.randint(1000, 9999)  # Advanced: four digits

    def decide_operation(self):
        # Randomly choose between addition and subtraction
        return random.choice(['+', '-'])

    def display_problem(self):
        # Generate random numbers and operation for the question
        self.num1 = self.random_int()
        self.num2 = self.random_int()
        self.operation = self.decide_operation()

        # Ensure that subtraction results in a non-negative answer
        if self.operation == '+' or self.num1 >= self.num2:
            self.correct_answer = eval(f"{self.num1} {self.operation} {self.num2}")
        else:
            self.correct_answer = eval(f"{self.num2} - {self.num1}")
            self.num1, self.num2 = self.num2, self.num1

        # Display the question
        question_text = f"{self.num1} {self.operation} {self.num2} = "
        self.question_label = tk.Label(self.root, text=question_text, font=("Arial", 14), bg="pink")
        self.question_label.pack(pady=10)

        # Create entry box for the user's answer
        self.answer_entry = tk.Entry(self.root, font=("Arial", 14))
        self.answer_entry.pack(pady=5)
        self.answer_entry.bind("<Return>", self.check_answer)  # Bind Enter key to check answer

    def check_answer(self, event=None):
        # Validate and check the user's answer
        try:
            user_answer = int(self.answer_entry.get())
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter a valid integer.")
            return

        # Check if the answer is correct
        if user_answer == self.correct_answer:
            # Award 10 points on first attempt, 5 on the second
            self.score += 10 if self.first_attempt else 5
            messagebox.showinfo("Correct", "Correct answer!")
            self.current_question += 1
            self.first_attempt = True  # Reset first attempt for the next question
            if self.current_question <= 10:
                self.next_question()  # Move to the next question
            else:
                self.display_results()  # Show results if 10 questions are completed
        else:
            if self.first_attempt:
                self.first_attempt = False  # Mark first attempt as used
                messagebox.showinfo("Try Again", "Incorrect. Try one more time.")
            else:
                # Show correct answer if second attempt fails
                messagebox.showinfo("Incorrect", f"The correct answer was {self.correct_answer}.")
                self.current_question += 1
                self.first_attempt = True  # Reset first attempt for the next question
                if self.current_question <= 10:
                    self.next_question()  # Move to the next question
                else:
                    self.display_results()  # Show results if 10 questions are completed

    def display_results(self):
        # Display final score and rank after quiz completion
        self.clear_window()
        rank = self.rank_score(self.score)  # Determine rank based on score
        result_text = f"Final Score: {self.score}/100\nRank: {rank}"
        
        # Show final score and rank
        tk.Label(self.root, text=result_text, font=("Arial", 16), bg="pink").pack(pady=10)
        tk.Button(self.root, text="Play Again", command=self.create_menu).pack(pady=5)
        tk.Button(self.root, text="Quit", command=self.root.quit).pack(pady=5)

    def rank_score(self, score):
        # Determine rank based on score
        if score > 90:
            return "A+"
        elif score > 80:
            return "A"
        elif score > 70:
            return "B"
        elif score > 60:
            return "C"
        elif score > 50:
            return "D"
        else:
            return "F"

    def next_question(self):
        # Clear the window and display the next question
        self.clear_window()
        self.display_problem()

    def clear_window(self):
        # Remove all widgets from the window
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = MathQuiz(root)
    root.mainloop()
 