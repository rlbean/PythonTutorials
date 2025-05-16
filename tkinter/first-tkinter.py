import tkinter as tk # starts out the visual app

def say_hello():
    label2.config(text="My favourite colour is " + entry.get())

window = tk.Tk() # creates the window
window.title("Bean's Great App!") # window title bar
window.geometry("400x300")  # Make the window bigger w x h

label = tk.Label(window, text="What is your favourite colour?")
label2 = tk.Label(window, text="")
label.pack()
label2.pack()

entry = tk.Entry(window) # text box entry 
entry.pack() # adds to the window and lays

button = tk.Button(window, text="Click Me", command=say_hello)
button.pack()

window.mainloop()









'''
def say_hello():
    label2.config(text="Your fav colour is " + entry.get())

window = tk.Tk() # creates the window
window.title("Bean's Great Python App!") # Title on window
window.geometry("400x200") # width x height

label = tk.Label(window, text="What's your favourite colour?")
label2 = tk.Label(window, text="")
label.pack()
label2.pack()

entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text="Click Me", command=say_hello)
button.pack()

window.mainloop() # keeps it running/open
'''