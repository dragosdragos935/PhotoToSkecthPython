import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def upload_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        image = cv2.imread(file_path)
        grey_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        invert = cv2.bitwise_not(grey_img)
        blur = cv2.GaussianBlur(invert, (21, 21), 0)
        invertedblur = cv2.bitwise_not(blur)
        sketch = cv2.divide(grey_img, invertedblur, scale=256.0)
        cv2.imwrite("sketch.png", sketch)
        display_image("sketch.png")

def display_image(image_path):
    image = Image.open(image_path)
    image.thumbnail((250, 250))
    img = ImageTk.PhotoImage(image)
    panel.config(image=img)
    panel.image = img

root = tk.Tk()
root.title("Photo to Sketch Converter")
root.geometry("300x300")

panel = tk.Label(root)
panel.pack(pady=10)

upload_button = tk.Button(root, text="Upload Image", command=upload_image)
upload_button.pack(pady=20)

root.mainloop()
