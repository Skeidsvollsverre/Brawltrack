import tkinter as tk
from tkinter import ttk

def create_matches_tab(tab):
    # Add some content to the Matches tab
    label = tk.Label(tab, text="This is the Matches tab", font=("Arial", 16))
    label.pack(pady=20)

def create_stats_tab(tab):
    # Add some content to the Stats tab
    label = tk.Label(tab, text="This is the Stats tab", font=("Arial", 16))
    label.pack(pady=20)

root = tk.Tk()
root.title("BRAWLTRACKER")

# Create the notebook and tabs
notebook = ttk.Notebook(root)
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
notebook.add(tab1, text="Matches")  # Tab1 for Matches
notebook.add(tab2, text="Stats")  # Tab2 for Stats
notebook.pack(fill="both", expand=True)

# Create content for each tab
create_matches_tab(tab1)
create_stats_tab(tab2)

root.minsize(width=400, height=400)
root.maxsize(width=800, height=800)

root.mainloop()