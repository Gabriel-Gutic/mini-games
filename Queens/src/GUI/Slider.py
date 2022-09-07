import tkinter as tk

from GUI.Object import Object
from GUI.Point import Point


class Slider(Object):
    def __init__(self, window, start=0, end=10, command=None, width=100, center=Point(0, 0)):
        super().__init__(window, width, center)
        
        self._scale = tk.Scale(window._window, from_=start, to=end, orient=tk.HORIZONTAL, command=command)
        self._scale.configure(width = width, relief = tk.FLAT)
        self._id = self._window.canvas.create_window(center.x, center.y, anchor=tk.NW, window=self._scale)
    
    def set(self, n):
        self._scale.set(n)
        
    def get(self):
        return int(self._scale.get())