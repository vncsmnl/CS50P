import unittest
from unittest.mock import patch
from io import StringIO
from tkinter import Tk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np
from project import BackgroundRemovalApp

class TestBackgroundRemovalApp(unittest.TestCase):

    def setUp(self):
        self.root = Tk()
        self.app = BackgroundRemovalApp(self.root)

    def tearDown(self):
        self.root.destroy()

    @patch('tkinter.filedialog.askopenfilename', return_value='test_image.jpg')
    @patch('rembg.remove', return_value=np.zeros((100, 100, 4), dtype=np.uint8))
    @patch('tkinter.filedialog.asksaveasfilename', return_value='output_image.png')
    def test_remove_background(self, mock_open, mock_remove, mock_save):
        self.app.remove_background()
        self.assertTrue(mock_open.called)
        self.assertTrue(mock_remove.called)
        self.assertTrue(mock_save.called)

    def test_update_display(self):
        image = Image.fromarray(np.zeros((100, 100, 4), dtype=np.uint8))
        self.app.update_display(image)
        self.assertIsInstance(self.app.label.cget('image'), ImageTk.PhotoImage)

    @patch('os.execl')
    @patch('sys.executable', 'python')
    @patch('sys.argv', ['script.py'])
    def test_restart_program(self, mock_execl):
        event = 'fake_event'
        self.app.restart_program(event)
        self.assertTrue(mock_execl.called)

    @patch('sys.executable', 'python')
    @patch('sys.argv', ['script.py'])
    def test_restart_program_without_event(self):
        self.app.restart_program(None)
        # Without an event, it should still restart without raising any errors

if __name__ == '__main__':
    unittest.main()
