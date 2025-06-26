# import tkinter as tk
# from time import strftime

# # Create main window
# root = tk.Tk()
# root.title("Digital Clock")
# root.geometry("350x150")
# root.configure(bg="black")

# # Create a label to display the time
# label = tk.Label(root, font=("Arial", 40, "bold"), background="black", foreground="cyan")
# label.pack(anchor="center")

# # Function to update the time
# def update_time():
#     current_time = strftime("%H:%M:%S")
#     label.config(text=current_time)
#     root.after(1000, update_time)  # call this function again after 1000ms

# update_time()
# root.mainloop()


import tkinter as tk
from datetime import datetime
import pytz  # Make sure to install with: pip install pytz

# Create the main window
root = tk.Tk()
root.title("World Digital Clock")
root.geometry("500x400")
root.configure(bg="#0f0f0f")  # Dark background

# Fonts and Colors
main_font = ("Courier", 30, "bold")
small_font = ("Arial", 16)
text_color = "#00FFCC"

# Labels
local_time_label = tk.Label(root, font=main_font, fg=text_color, bg="#0f0f0f")
local_time_label.pack(pady=10)

date_label = tk.Label(root, font=small_font, fg="lightgray", bg="#0f0f0f")
date_label.pack(pady=5)

world_frame = tk.Frame(root, bg="#0f0f0f")
world_frame.pack(pady=20)

ny_label = tk.Label(world_frame, font=small_font, fg="orange", bg="#0f0f0f")
ny_label.pack(pady=2)

london_label = tk.Label(world_frame, font=small_font, fg="skyblue", bg="#0f0f0f")
london_label.pack(pady=2)

tokyo_label = tk.Label(world_frame, font=small_font, fg="violet", bg="#0f0f0f")
tokyo_label.pack(pady=2)

def update_clock():
    now = datetime.now()
    local_time = now.strftime("%H:%M:%S")
    date = now.strftime("%A, %d %B %Y")

    # Local time
    local_time_label.config(text=f"Local Time: {local_time}")
    date_label.config(text=f"Date: {date}")

    # World Times
    ny = datetime.now(pytz.timezone("America/New_York")).strftime('%H:%M:%S')
    london = datetime.now(pytz.timezone("Europe/London")).strftime('%H:%M:%S')
    tokyo = datetime.now(pytz.timezone("Asia/Tokyo")).strftime('%H:%M:%S')

    ny_label.config(text=f"New York: {ny}")
    london_label.config(text=f"London: {london}")
    tokyo_label.config(text=f"Tokyo: {tokyo}")

    root.after(1000, update_clock)  # Update every second

# Start the clock
update_clock()
root.mainloop()

