import tkinter as tk

def login_results():
    label2.config(text="Thanks for signing in " + username_entry.get())

window = tk.Tk()
window.title("Login Form")
window.geometry("300x150")

tk.Label(window, text="Username:").grid(row=0, column=0, padx=10, pady=5) # combine 2 lines
username_entry = tk.Entry(window)
username_entry.grid(row=0, column=1)

tk.Label(window, text="Password:").grid(row=1, column=0, padx=10, pady=5)
password_entry = tk.Entry(window)
password_entry.grid(row=1, column=1)

login_button = tk.Button(window, text="Login",command=login_results)
login_button.grid(row=2, column=0, columnspan=2, pady=10)

label2 = tk.Label(window, text="")
label2.grid(row=3, column=0, columnspan=2,  padx=10, pady=5)

window.mainloop()











'''
import tkinter as tk

window = tk.Tk()
window.title("Login Form")
window.geometry("300x150")

tk.Label(window, text="Username:").grid(row=0, column=0, padx=10, pady=5)
username_entry = tk.Entry(window)
username_entry.grid(row=0, column=1)

tk.Label(window, text="Password:").grid(row=1, column=0, padx=10, pady=5)
password_entry = tk.Entry(window)
password_entry.grid(row=1, column=1)

login_button = tk.Button(window, text="Login")
login_button.grid(row=2, column=0, columnspan=2, pady=10)

window.mainloop()
'''