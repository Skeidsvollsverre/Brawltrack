import tkinter as tk
from tkinter import ttk
import requests
import json

# Function to get data from the Brawlhalla API
def get_brawlhalla_data(brawlhalla_id):
    api_key = 'YOUR_API_KEY'  # Replace with your actual API key
    url = f"https://api.brawlhalla.com/player/{brawlhalla_id}/ranked?api_key={api_key}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()  # Return the JSON data
    else:
        return None

# Function to display player information in the Tkinter window
def display_player_data():
    player_id = player_id_entry.get()
    
    player_data = get_brawlhalla_data(player_id)
    
    if player_data:
        # Display player details
        player_info.config(text=f"Name: {player_data['name']}\n"
                                f"Rating: {player_data['rating']}\n"
                                f"Peak Rating: {player_data['peak_rating']}\n"
                                f"Tier: {player_data['tier']}\n"
                                f"Wins: {player_data['wins']}\n"
                                f"Games: {player_data['games']}\n"
                                f"Region: {player_data['region']}\n"
                                f"Global Rank: {player_data['global_rank']}\n"
                                f"Region Rank: {player_data['region_rank']}")

        # Display legend information
        legends_info.config(text="")
        for legend in player_data['legends']:
            legends_info.config(text=legends_info.cget("text") + 
                                f"Legend: {legend['legend_name_key']} \n"
                                f"Rating: {legend['rating']}\n"
                                f"Peak Rating: {legend['peak_rating']}\n"
                                f"Tier: {legend['tier']}\n"
                                f"Wins: {legend['wins']}\n"
                                f"Games: {legend['games']}\n\n")
    else:
        player_info.config(text="Player not found or error fetching data.")

# Create the main Tkinter window
root = tk.Tk()
root.title("Brawlhalla Ranked Data")
root.geometry("500x600")

# Label and entry for Brawlhalla player ID
player_id_label = tk.Label(root, text="Enter Brawlhalla ID:")
player_id_label.pack(pady=10)

player_id_entry = tk.Entry(root)
player_id_entry.pack(pady=10)

# Button to fetch and display data
fetch_button = tk.Button(root, text="Get Ranked Data", command=display_player_data)
fetch_button.pack(pady=10)

# Label to display player info
player_info = tk.Label(root, text="", justify="left")
player_info.pack(pady=10)

# Label to display legends info
legends_info = tk.Label(root, text="", justify="left")
legends_info.pack(pady=10)

root.mainloop()
