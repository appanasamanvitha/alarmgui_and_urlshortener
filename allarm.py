import tkinter as tk
import time
from tkinter import messagebox
from playsound import playsound
from PIL import ImageTk,Image

def set_alarm():
    alarm_time = entry.get()
    current_time = time.strftime('%H:%M')
    while current_time != alarm_time:
        current_time = time.strftime('%H:%M')
        time.sleep(1)
    playsound("C:\\Users\\admin\\Downloads\\clean-trap-loop-131bpm-136738.mp3")
    messagebox.showinfo("Alarm", "Wake up!")

# Create the main window
window = tk.Tk()
window.title("Alarm")
window.resizable(True, True)



# Create a label and entry for setting the alarm time
label = tk.Label(window, text="Enter alarm time (HH:MM):")
label.pack()
entry = tk.Entry(window)
entry.pack()

# Create a button to set the alarm
button = tk.Button(window, text="Set Alarm", command=set_alarm)
button.pack()

# Start the main event loop
window.mainloop()
