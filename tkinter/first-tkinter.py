import tkinter as tk # starts out the visual app

window = tk.Tk() # creates the window
window.title("Bean's Great App!") # window title bar

label = tk.Label(window, text="Hello World!")
label2 = tk.Label(window, text="Message 2")
label2.pack()
label.pack()


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