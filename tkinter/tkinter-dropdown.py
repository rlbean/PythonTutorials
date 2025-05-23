import tkinter as tk
from PIL import Image, ImageTk

# Mood-to-image mapping
mood_images = {
    "Happy": "assets/smiling_128.png",
    "Sad": "assets/sad_128.png",
    "Angry": "assets/angry_128.png",
    "Surprised": "assets/surprised_128.png"
}

# Map to icon images
mood_icons = {
    "Happy": "assets/smiling_128.png",
    "Sad": "assets/sad_128.png",
    "Angry": "assets/angry_128.png",
    "Surprised": "assets/surprised_128.png"
}

def update_image(*args):
    selected_mood = mood_var.get() # get the mood
    file_name = mood_images[selected_mood] # get the image path
    image = Image.open(file_name) # open file
    image = image.resize((150, 150)) # resize the image to fit
    photo = ImageTk.PhotoImage(image) # get it ready to display
    image_label.config(image=photo)
    image_label.image = photo # keep a reference


#create window
window = tk.Tk()
window.title("Mood Selector")
window.geometry("300x300")
window.configure(bg="white") # Set background

#Mood dropdown
mood_var = tk.StringVar(window)
mood_var.set("Happy") # Default option

# This calls update_image automatically when mood_var changes
mood_var.trace_add("write", update_image)

dropdown = tk.OptionMenu(window, mood_var, *mood_images.keys())
dropdown.pack(pady=10)

# Button to update image
show_button = tk.Button(window, text="Show Mood", command=update_image)
show_button.pack(pady=10)

#Label to display the image
image_label = tk.Label(window, bg="blue")
image_label.pack(pady=10)
update_image()
window.mainloop()