import tkinter as tk


class Window:
    def __init__(self, title="", width=1280, height=720):
        self._window = tk.Tk("Soarecele prin labirint")
        self._window.title(title)

        self.set_resizable(False)

        self._canvas = tk.Canvas(self._window, width=width, height=height)
        self._canvas.pack()
    
    def get(self):
        return self._window
    
    def run(self):
        self._window.mainloop()
    
    @property
    def canvas(self):
        return self._canvas
    
    def set_resizable(self, resizable : bool):
        self._window.resizable(resizable, resizable)