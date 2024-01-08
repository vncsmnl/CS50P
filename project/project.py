import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import rembg
import numpy as np
import sys
import os

class BackgroundRemovalApp:
    def __init__(self, root):
        self.root = root
        root.title("Remove Background")

        # Create a label to display the image
        self.label = tk.Label(root)
        self.label.pack(padx=10, pady=10)

        # Create a button to initiate background removal and image saving
        remove_button = tk.Button(root, text="Start Here", command=self.remove_background)
        remove_button.pack(pady=10)

        # Associate the F5 keypress event with the program restart function
        root.bind("<F5>", self.restart_program)

    def remove_background(self):
        # Open a dialog to select an image
        file_path = filedialog.askopenfilename()

        if file_path:
            try:
                # Load the image using the PIL library
                image = Image.open(file_path)

                # Convert the image to a format accepted by rembg
                image_array = np.array(image)
                output = rembg.remove(image_array)

                # Convert the rembg output back to a PIL image
                output_image = Image.fromarray(output)

                # Save the image with the removed background
                save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
                if save_path:
                    output_image.save(save_path)

                # Update the image displayed in the interface
                self.update_display(output_image)

            except Exception as e:
                # Handle errors, e.g., when the selected file is not an image
                print(f"Error: {e}")

    def update_display(self, image):
        # Update the displayed image in the interface
        photo = ImageTk.PhotoImage(image)
        self.label.config(image=photo)
        self.label.image = photo

    def restart_program(self, event):
        # Restart the program
        python = sys.executable
        os.execl(python, python, *sys.argv)

def main():
    root = tk.Tk()
    app = BackgroundRemovalApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
