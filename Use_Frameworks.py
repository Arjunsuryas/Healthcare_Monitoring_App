import tkinter as tk

# Global "window" simulation
class GlobalWindow:
    framework_ready = None

window = GlobalWindow()

def use_framework_ready(callback):
    """Simulate calling a frameworkReady callback once on initialization."""
    if callable(window.framework_ready):
        window.framework_ready()
    callback()

# Example usage
def on_framework_ready():
    print("Framework is ready!")

window.framework_ready = on_framework_ready

root = tk.Tk()
root.title("Framework Ready Example")
root.geometry("300x200")

# Call our hook simulation
use_framework_ready(lambda: print("Initializing app..."))

label = tk.Label(root, text="Hello, Tkinter!", font=("Helvetica", 16))
label.pack(pady=50)

root.mainloop()
