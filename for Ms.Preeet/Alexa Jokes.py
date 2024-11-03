import tkinter as tk
import random

class JokeApp:
    def __init__(self, root):
        # Set up the main window and set the background color to pink
        self.root = root
        self.root.title("Alexa, tell me a Joke!")
        self.root.configure(bg="pink")  # Set background color to pink

        # Load jokes from the text file
        self.jokes = self.load_jokes()

        # Label for displaying the joke setup (initially prompts the user)
        self.setup_label = tk.Label(root, text="Press 'New Joke' to start!", font=("Arial", 14), bg="pink")
        self.setup_label.pack(pady=10)

        # Label for displaying the punchline, styled in italic and initially empty
        self.punchline_label = tk.Label(root, text="", font=("Arial", 14, "italic"), fg="gray", bg="pink")
        self.punchline_label.pack(pady=10)

        # Button to get a new joke, calling display_setup when clicked
        self.next_joke_button = tk.Button(root, text="New Joke", command=self.display_setup)
        self.next_joke_button.pack(pady=5)

        # Button to show the punchline, calling display_punchline when clicked, initially disabled
        self.show_punchline_button = tk.Button(root, text="Show Punchline", command=self.display_punchline, state=tk.DISABLED)
        self.show_punchline_button.pack(pady=5)

        # Button to quit the application
        self.quit_button = tk.Button(root, text="Quit", command=root.quit)
        self.quit_button.pack(pady=5)

    def load_jokes(self):
        # Load jokes from the text file and split each line at '?'
        jokes = []
        try:
            with open(r"C:\Users\cylea\SCHOOL L5\for Ms.Preeet\exercise 2 notes\randomjokes.txt", "r") as file:
                # For each line, split the setup and punchline at '?'
                jokes = [line.strip().split('?') for line in file if '?' in line]
        except FileNotFoundError:
            # Default joke if the file is not found
            jokes = [("Why don't skeletons fight each other", "They don't have the guts")]
        return jokes

    def display_setup(self):
        # Choose a random joke and display only the setup part
        self.current_joke = random.choice(self.jokes)  # Select a random joke
        self.setup_label.config(text=self.current_joke[0] + "?")  # Show the setup
        self.punchline_label.config(text="")  # Clear the previous punchline
        self.show_punchline_button.config(state=tk.NORMAL)  # Enable the "Show Punchline" button

    def display_punchline(self):
        # Display the punchline and disable the "Show Punchline" button
        self.punchline_label.config(text=self.current_joke[1])  # Show the punchline
        self.show_punchline_button.config(state=tk.DISABLED)  # Disable the button to prevent repeat

# Initialize the main Tkinter window and start the app
root = tk.Tk()
app = JokeApp(root)
root.mainloop()
