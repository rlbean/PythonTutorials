import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("TTK Demo")
window.geometry("400x250")
window.resizable(False, False) # makes the window not resizeable

#Create a style and set a theme
style = ttk.Style()
style.theme_use('adapta') # clam, alt, default, classic

#Add Label

label = ttk.Label(window, text="Enter your name: ")
label.pack(pady=10)

#Entry widget
name_var = tk.StringVar()
entry = ttk.Entry(window, textvariable=name_var, width=30)
entry.pack(pady=5)

# Add Progress Bar
progress = ttk.Progressbar(window, length=200, mode="determinate")
progress.pack(pady=20)

# Action for the button
def say_hello():
    username = name_var.get()
    if username:
        greeting_label.config(text=f"Hello, {username}!")
        progress.start(10)
    else:
        greeting_label.config(text="Please enter your name.")
        progress.stop()

# Button
btn = ttk.Button(window, text="Submit", command=say_hello)
btn.pack(pady=10)

# Label for greeting
greeting_label = ttk.Label(window, text="")
greeting_label.pack(pady=5)



window.mainloop()