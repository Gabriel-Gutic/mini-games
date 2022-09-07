import tkinter as tk

from GUI.Point import Point


class Button:
    def __init__(self, window, command=None, text='Button', width=20, height=2, center=Point(0, 0)):
        self._window = window
        self._button = tk.Button(window.get(), text=text, command=command)
        self._button.configure(width=width, height=height, bg='lightgray', fg='black')
        self._id = self._window.canvas.create_window(center.x, center.y, window=self._button)

    def set_visible(self, visible):
        if visible:
            self._window.canvas.itemconfigure(self._id, state='normal')
        else:
            self._window.canvas.itemconfigure(self._id, state='hidden')