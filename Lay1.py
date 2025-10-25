import tkinter as tk
from tkinter import messagebox

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Root Layout")
        self.geometry("400x300")
        self.configure(bg="white")

        # Simulate "framework ready" hook
        self.framework_ready()

        # Initialize main container
        self.container = tk.Frame(self, bg="white")
        self.container.pack(fill="both", expand=True)

        # Show the not-found screen
        self.show_not_found()

        # Status bar
        self.status_bar = tk.Label(self, text="Status: Auto", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side="bottom", fill="x")

    def framework_ready(self):
        # Placeholder for any initialization logic
        print("Framework is ready!")

    def show_not_found(self):
        # Clear container
        for widget in self.container.winfo_children():
            widget.destroy()

        tk.Label(self.container, text="Oops!", font=("Helvetica", 20), bg="white").pack(pady=20)
        tk.Label(self.container, text="This screen doesn't exist.", bg="white").pack(pady=10)
        tk.Button(
            self.container, 
            text="Go to Home Screen", 
            command=self.go_home
        ).pack(pady=10)

    def go_home(self):
        messagebox.showinfo("Home", "Returning to Home Screen...")

if __name__ == "__main__":
    app = App()
    app.mainloop()
