import tkinter as tk

root = tk.Tk()
root.title("BRAWLTRACKER")

root.minsize(width=400, height=400)
root.maxsize(width=800, height=800)

# Configure the grid to have at least 3 columns
root.grid_columnconfigure(0, weight=1)  # Empty space on the left
root.grid_columnconfigure(1, weight=1)  # Buttons
root.grid_columnconfigure(2, weight=1)  # Empty space on the right

# Center the Matches button and make it larger
btn_matches = tk.Button(root, text="Matches", width=15, height=3)  # Increase width and height
btn_matches.grid(row=0, column=1, sticky="wn")

# Center the Stats button below the Matches button and make it larger
btn_stats = tk.Button(root, text="Stats", width=15, height=3)  # Increase width and height
btn_stats.grid(row=0, column=2, sticky="ne")

root.mainloop()


