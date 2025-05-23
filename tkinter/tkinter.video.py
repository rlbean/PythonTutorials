import tkinter as tk
import cv2
from PIL import Image, ImageTk

window = tk.Tk()
window.title("Video Player")
window.geometry("640x480")

# Open video file
cap = cv2.VideoCapture("assets/video-movement-physics.mp4")

#Create label to display video
video_label = tk.Label(window)
video_label.pack()

def update_frame():
    ret, frame = cap.read()
    if ret:
        #Convert BGR (OpenCV) to RGB (PIL)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image = img)
        video_label.imgtk = imgtk
        video_label.config(image=imgtk)
    window.after(30, update_frame) # Update every  30 ms (~30fps)

update_frame()
window.mainloop()
cap.release()