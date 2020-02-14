"""
The bare minimum to draw to screen, and creating the screen.
This is the only use of another GUI/Graphic library since raw python cant do this.
"""

import tkinter as TK

from PyRay.color import Color
from copy import deepcopy


class Screen(object):
    """
    A screen, used to display stuff.
    """

    def __init__(self, width: int, height: int):
        self.width, self.height = width, height
        self._closed = False
        
        self._pixels = [[Color("white") for _ in range(width)] for _ in range(height)]
        self._old_pixels = [[Color("black") for _ in range(width)] for _ in range(height)]
        self._setup_canvas()
        self._draw_screen()

    def _setup_canvas(self):
        self._master = TK.Tk()
        self._canvas = TK.Canvas(self._master, width=self.width, height=self.height)
        self._canvas.pack()
        self._master.protocol("WM_DELETE_WINDOW", self._window_closed)

    @staticmethod
    def _copy_pixel_list(pixels):
        """
        Custom copy methods since swallow is not deep enough and,
        Deep is to slow and takes to much.
        :param pixels:
        :return:
        """
        return [column.copy() for column in pixels]

    def _window_closed(self):
        self._closed = True

    @property
    def size(self):
        return self.width, self.height

    def set_pixel(self, x: int, y: int, color: Color):  # TODO: make a Color Class
        self._pixels[x][y] = Color(color)

    def _set_pixel_at_screen(self, x: int, y: int, color: Color):  # TODO: make a Color Class
        """
        Set a pixel of the screen
        :param x: The x cord
        :param y:  The y cord
        :param color: The color Class (string for now)
        :return:
        """
        self._canvas.create_rectangle((x, y, x, y), fill=str(color), outline="")  # trick to set one pixel of a Canvas.

    def _draw_screen(self):
        for x, columns in enumerate(self._pixels):
            for y, color in enumerate(columns):
                if self._old_pixels[x][y] != color:
                    self._set_pixel_at_screen(x, y, color)
        self._old_pixels = self._copy_pixel_list(self._pixels)

    def update(self):
        """
        Update the screen with the new data.
        Raises a Warning if the window has been closed.
        :return:
        """

        self._draw_screen()
        if not self._closed:
            self._master.update()
        else:
            raise Warning("Screen.update() called on a closed window, ignoring.")
