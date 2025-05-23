import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
window.title("Image Viewer")
window.geometry("400x400")

# Load the image
image = Image.open("assets/dogs.jpg")
photo = ImageTk.PhotoImage(image)

#Display the image in a label
label = tk.Label(window, image=photo)
label.pack()

window.mainloop()