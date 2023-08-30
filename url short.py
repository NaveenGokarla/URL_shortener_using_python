import tkinter as tk
import pyshorteners
import webbrowser

def shorten_url():
    long_url = input_field.get()
    type_tiny = pyshorteners.Shortener()
    short_url = type_tiny.tinyurl.short(long_url)
    
    display_text.config(text="Click to open the Shortened URL:")
    link = tk.Label(root, text=short_url, fg="blue", cursor="hand2")
    link.bind("<Button-1>", lambda e: webbrowser.open(short_url))
    link.pack(pady=5)

# Create the main window
root = tk.Tk()
root.title("URL Shortener")

# Maximize the window
root.state('zoomed')

# Create an input field
input_field = tk.Entry(root)
input_field.pack(pady=10)

# Create a submit button
submit_button = tk.Button(root, text="Shorten URL", command=shorten_url)
submit_button.pack()

# Create a text label
display_text = tk.Label(root, text="")
display_text.pack(pady=10)

# Start the main loop
root.mainloop()
