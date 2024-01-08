#### Video Demo:  <URL HERE>
#### Description:

# Remove Background GUI

This simple Python script uses the Tkinter library to create a graphical user interface (GUI) for removing backgrounds from images using the `rembg` library. The script allows users to select an image file, removes the background, and then saves the result as a PNG file.

## Prerequisites

Before running the script, make sure you have the following dependencies installed:

- [Python](https://www.python.org/downloads/) (the script is compatible with Python 3)
- [Tkinter](https://docs.python.org/3/library/tkinter.html) (usually included with Python)
- [PIL](https://python-pillow.org/) (Python Imaging Library)
- [rembg](https://pypi.org/project/rembg/) (to remove the background)

You can install the required Python packages using the following command:

```bash
pip install -r requirements.txt
```

## How to Use

1. Run the script by executing the following command in your terminal:

```bash
python project.py
```

2. The GUI window will appear with a "Start Here" button.

3. Click the "Start Here" button to open a file dialog and select an image file.

4. The script will attempt to remove the background from the selected image and display the result in the GUI.

5. Optionally, press F5 to restart the program.

## Notes

- If the selected file is not an image or if any errors occur during the process, an error message will be printed in the terminal.

- The script uses the F5 key as a shortcut to restart the program.

- The output image will be saved in PNG format.

Feel free to modify the script according to your needs or contribute to its development. If you encounter any issues, please check the error messages in the terminal for more information.
