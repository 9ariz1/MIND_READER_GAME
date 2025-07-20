import tkinter as tk
from tkinter import ttk, messagebox
import time
import threading

def center_window(window, width, height):
    root.update_idletasks()
    x = root.winfo_x() + (root.winfo_width() // 2) - (width // 2)
    y = root.winfo_y() + (root.winfo_height() // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")

def start_mind_reading():
    try:
        number = int(entry.get())
        if not 1 <= number <= 1000:
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a number between 1 and 1000.", parent=root)
        return

    def process():
        steps = [
            "Analyzing Brainwaves...",
            "Scanning Memories...",
            "Calculating Probabilities...",
            "Decoding Thoughts...",
        ]

        progress_win = tk.Toplevel(root)
        progress_win.title("Reading Your Brain")
        center_window(progress_win, 350, 120)
        progress_win.transient(root)
        progress_win.grab_set()

        progress_label = tk.Label(progress_win, text="Starting mind reading...", font=("Arial", 11))
        progress_label.pack(pady=10)

        progress = ttk.Progressbar(progress_win, orient=tk.HORIZONTAL, length=300, mode='determinate')
        progress.pack(pady=10)
        
        for i in range(100):
            time.sleep(0.05)
            progress["value"] = i + 1
            if i % 25 == 0 and i // 25 < len(steps):
                progress_label.config(text=steps[i // 25])
            progress_win.update()

        progress_win.destroy()
        root.after(100, lambda: messagebox.showinfo("Mind Reading Complete", f"You're Thinking of the number {number}", parent=root))

    threading.Thread(target=process).start()

# GUI setup
root = tk.Tk()
root.title("Mind Reader")
root.geometry("400x200")

heading = tk.Label(root, text="Think of a number between 1 to 1000:", font=("Arial", 14))
heading.pack(pady=20)

entry = tk.Entry(root, font=("Arial", 12), justify="center")
entry.pack(pady=5)

read_button = tk.Button(root, text="Read My Mind", font=("Arial", 12), command=start_mind_reading)
read_button.pack(pady=20)

root.mainloop()
