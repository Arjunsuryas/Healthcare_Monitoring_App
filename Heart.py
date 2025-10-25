import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from dataclasses import dataclass, asdict
from typing import List, Optional
import json
import os
from datetime import datetime
import random

STORAGE_FILE = "heart_readings.json"

@dataclass
class Reading:
    heart_rate: int
    blood_pressure: dict
    timestamp: str

# Load and save readings
def load_readings() -> List[Reading]:
    if not os.path.exists(STORAGE_FILE):
        return []
    with open(STORAGE_FILE, "r") as f:
        data = json.load(f)
        return [Reading(**r) for r in data]

def save_readings(readings: List[Reading]):
    # Keep only last 10 readings
    readings_to_save = readings[:10]
    with open(STORAGE_FILE, "w") as f:
        json.dump([asdict(r) for r in readings_to_save], f, indent=2)

# Heart rate and BP categories
def get_heart_rate_category(rate: int):
    if rate < 60:
        return ("Low", "#EF4444")
    if rate <= 100:
        return ("Normal", "#10B981")
    return ("High", "#EF4444")

def get_bp_category(systolic: int, diastolic: int):
    if systolic < 120 and diastolic < 80:
        return ("Normal", "#10B981")
    if systolic <= 129 and diastolic < 80:
        return ("Elevated", "#F59E0B")
    if systolic <= 139 or diastolic <= 89:
        return ("Stage 1", "#EF4444")
    return ("Stage 2", "#DC2626")

# Main app
class HeartMonitorApp:
    def __init__(self, root):
        self.root = root
        root.title("Heart Monitor")
        root.geometry("500x400")

        self.readings: List[Reading] = load_readings()
        self.is_monitoring = False
        self.heart_rate = 0
        self.progress = 0

        self.hr_label = ttk.Label(root, text="Heart Rate: -- bpm", font=("Helvetica", 16))
        self.hr_label.pack(pady=10)

        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(root, maximum=100, variable=self.progress_var)
        self.progress_bar.pack(fill="x", padx=20, pady=10)

        self.start_btn = ttk.Button(root, text="Start Monitoring", command=self.start_monitoring)
        self.start_btn.pack(pady=5)

        self.bp_btn = ttk.Button(root, text="Enter Blood Pressure", command=self.enter_bp)
        self.bp_btn.pack(pady=5)

        self.tree = ttk.Treeview(root, columns=("HR", "BP", "Time", "HR Category", "BP Category"), show="headings")
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)
        self.load_tree()

    def load_tree(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        for r in self.readings:
            hr_cat, hr_color = get_heart_rate_category(r.heart_rate)
            bp_cat, bp_color = get_bp_category(r.blood_pressure["systolic"], r.blood_pressure["diastolic"])
            self.tree.insert("", "end", values=(
                r.heart_rate,
                f"{r.blood_pressure['systolic']}/{r.blood_pressure['diastolic']}",
                r.timestamp,
                hr_cat,
                bp_cat
            ))

    def start_monitoring(self):
        if self.is_monitoring:
            return
        self.is_monitoring = True
        self.progress = 0
        self.heart_rate = 0
        self.hr_label.config(text="Heart Rate: -- bpm")
        self.update_progress()

    def update_progress(self):
        if not self.is_monitoring:
            return
        if self.progress >= 100:
            self.is_monitoring = False
            self.heart_rate = random.randint(60, 100)
            self.hr_label.config(text=f"Heart Rate: {self.heart_rate} bpm")
            return
        self.progress += 6.67  # ~15 seconds total
        self.progress_var.set(self.progress)
        self.root.after(1000, self.update_progress)

    def enter_bp(self):
        if self.heart_rate == 0:
            messagebox.showerror("Error", "Please measure heart rate first")
            return
        systolic = simpledialog.askinteger("Systolic", "Enter systolic value:")
        diastolic = simpledialog.askinteger("Diastolic", "Enter diastolic value:")
        if systolic is None or diastolic is None:
            return
        reading = Reading(
            heart_rate=self.heart_rate,
            blood_pressure={"systolic": systolic, "diastolic": diastolic},
            timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
        self.readings = [reading] + self.readings[:9]  # Keep last 10
        save_readings(self.readings)
        self.load_tree()

root = tk.Tk()
app = HeartMonitorApp(root)
root.mainloop()
