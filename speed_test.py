import tkinter as tk
import random
import time

class SpeedTypingTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Speed Typing Test")

        self.sentences = [
            "The quick brown fox jumps over the lazy dog.",
            "Programming is the art of telling another human being what one wants the computer to do.",
            "Success is not final, failure is not fatal: it is the courage to continue that counts.",
            "In the end, we will remember not the words of our enemies, but the silence of our friends."
        ]

        self.sentence = random.choice(self.sentences)
        self.label = tk.Label(root, text=self.sentence, font=("Arial", 18))
        self.label.pack(pady=20)

        self.entry = tk.Entry(root, font=("Arial", 16))
        self.entry.pack(pady=20)

        self.start_time = None
        self.submit_button = tk.Button(root, text="Start Typing", font=("Arial", 16), command=self.start_typing)
        self.submit_button.pack(pady=20)

        self.result_label = tk.Label(root, text="", font=("Arial", 14))
        self.result_label.pack(pady=20)

    def start_typing(self):
        if self.start_time is None:
            self.start_time = time.time()
            self.submit_button.config(text="Submit")
        else:
            user_input = self.entry.get()
            elapsed_time = time.time() - self.start_time
            words_typed = len(user_input.split())
            words_per_minute = (words_typed / elapsed_time) * 60
            correct = user_input == self.sentence
            self.display_result(correct, words_per_minute)

    def display_result(self, correct, words_per_minute):
        if correct:
            self.result_label.config(text=f"Correct! Your speed: {words_per_minute:.2f} WPM", fg="green")
        else:
            self.result_label.config(text=f"Incorrect. Your speed: {words_per_minute:.2f} WPM", fg="red")

# Create the main window
root = tk.Tk()
root.geometry("1000x500")  # Set the window size
root.resizable(False, False)  # Disable window resizing

# Create an instance of the SpeedTypingTest class
speed_typing_test = SpeedTypingTest(root)

# Start the Tkinter main loop
root.mainloop()
