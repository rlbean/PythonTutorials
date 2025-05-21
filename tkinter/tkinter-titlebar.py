import tkinter as tk

#functions for buttons
def close_app():
    window.destroy()

window = tk.Tk()
window.geometry("400x300")
#window.overrideredirect(True) # hide our title bar

# fake title bar
title_bar = tk.Frame(window, bg="darkblue", relief="raised", bd="2")
title_bar.pack(fill=tk.X)

title_Label = tk.Label(title_bar, text="My Custom Title", bg="darkblue", fg="white", font=("Arial", "14"))
title_Label.pack(side=tk.LEFT)

#control buttons
btn_close = tk.Button(title_bar, text="X", command=close_app, bg="red", fg="white", bd=2, padx=10)
btn_close.pack(side=tk.RIGHT)

window.configure(bg="lightblue")

window.mainloop()

