import tkinter as tk
from tkinter import messagebox

class NotFoundScreen(tk.Frame):
    def __init__(self, master, go_home_callback):
        super().__init__(master)
        self.master = master
        self.go_home_callback = go_home_callback
        self.configure(bg="white")
        self.pack(fill="both", expand=True, padx=20, pady=20)

        # Title
        title_label = tk.Label(self, text="Oops!", font=("Helvetica", 24, "bold"), bg="white")
        title_label.pack(pady=(0, 20))

        # Message
        message_label = tk.Label(self, text="This screen doesn't exist.", font=("Helvetica", 16), bg="white")
        message_label.pack(pady=(0, 15))

        # Link / Button to go home
        home_btn = tk.Button(
            self,
            text="Go to home screen!",
            command=self.go_home,
            bg="#3B82F6",
            fg="white",
            font=("Helvetica", 14),
            padx=10,
            pady=10
        )
        home_btn.pack(pady=10)

    def go_home(self):
        # Call the callback to return to home screen
        self.go_home_callback()
        messagebox.showinfo("Navigation", "Returning to Home Screen...")

# Example usage
if __name__ == "__main__":
    def go_home():
        print("Navigating to home screen...")

    root = tk.Tk()
    root.title("Not Found")
    root.geometry("400x300")
    NotFoundScreen(root, go_home)
    root.mainloop()
