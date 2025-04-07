import tkinter as tk
import random
import string
import time

class BruteForceSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Brute Force Simulator")

        self.label = tk.Label(root, text="Enter your password:")
        self.entry = tk.Entry(root, show="*")
        self.crack_button = tk.Button(root, text="Simulate Brute Force", command=self.simulate_brute_force)

        self.label.pack(pady=10)
        self.entry.pack(pady=10)
        self.crack_button.pack(pady=10)

    def simulate_brute_force(self):
        user_password = self.entry.get()
        password_generation_window = self.show_password_generation(user_password)
        guessed_password, iterations, time_taken = self.brute_force(user_password, password_generation_window)
        password_generation_window.destroy()
        self.show_final_result(user_password, guessed_password, iterations, time_taken)

    def brute_force(self, user_password, password_generation_window):
        password_set = string.ascii_letters + string.digits + string.punctuation
        guessed_password = ""
        start_time = time.time()

        for attempt in range(1, 5000000):  # Increase attempts for faster simulation
            guessed_password = "".join(random.choice(password_set) for _ in range(len(user_password)))
            password_generation_window.update_idletasks()

            # Display the current attempt number in the password generation window
            password_generation_window.title(f"Attempt: {attempt}")

            if guessed_password == user_password:
                break

        end_time = time.time()
        iterations = attempt
        time_taken = end_time - start_time

        return guessed_password, iterations, time_taken

    def show_password_generation(self, user_password):
        password_generation_window = tk.Toplevel(self.root)
        password_generation_window.title("Password Generation")

        attempt_label = tk.Label(password_generation_window, text="Attempt: 0")
        password_label = tk.Label(password_generation_window, text="Generated Password:")
        generated_password = tk.Label(password_generation_window, text="")

        attempt_label.pack(pady=10)
        password_label.pack(pady=10)
        generated_password.pack(pady=10)

        password_set = string.ascii_letters + string.digits + string.punctuation

        for attempt in range(1, 5000000):  # Display 50 attempts
            generated_password_text = "".join(random.choice(password_set) for _ in range(len(user_password)))
            generated_password.config(text=generated_password_text)
            attempt_label.config(text=f"Attempt: {attempt}")
            password_generation_window.update_idletasks()

            if generated_password_text == user_password:
                break

        return password_generation_window

    def show_final_result(self, user_password, guessed_password, iterations, time_taken):
        final_popup = tk.Toplevel(self.root)
        final_popup.title("Simulation Result")

        result_label = tk.Label(final_popup, text="Simulation Result", font=("Helvetica", 16, "bold"))
        result_label.pack(pady=10)

        if guessed_password == user_password:
            message = f"Password successfully cracked!\n\nCracked Password: {guessed_password}\nIterations: {iterations}\nTime Taken: {time_taken:.4f} seconds"
        else:
            message = f"Password not cracked. Try increasing attempts.\nIterations: {iterations}\nTime Taken: {time_taken:.4f} seconds"

        result_text = tk.Label(final_popup, text=message)
        result_text.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = BruteForceSimulator(root)
    root.mainloop()
