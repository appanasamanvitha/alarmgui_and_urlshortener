import tkinter as tk
import pyshorteners

def shorten_url():
    long_url = entry.get()
    shortener = pyshorteners.Shortener()
    shortened_url = shortener.tinyurl.short(long_url)
    result_label.config(text="Shortened URL: " + shortened_url)

# Create the Tkinter window
window = tk.Tk()
window.title("URL Shortener")

# Create and position the widgets
label = tk.Label(window, text="Enter the URL:")
label.pack()

entry = tk.Entry(window, width=50)
entry.pack()

button = tk.Button(window, text="Shorten", command=shorten_url)
button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

# Run the Tkinter main loop
window.mainloop()
