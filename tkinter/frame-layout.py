import tkinter as tk

window = tk.Tk()
window.title("Frame Example")
window.geometry("400x300")

# Create a frame for the top part
top_frame = tk.Frame(window, bg="lightblue")
top_frame.pack(fill=tk.X)

# Add widgets to the frame
tk.Label(top_frame, text="Header", bg="lightblue", font=("Arial", 16)).pack(pady=10)

# Create a frame for main content
main_frame = tk.Frame(window)
main_frame.pack(pady=20)

tk.Label(main_frame, text="Content goes here.").pack()


window.mainloop()