from PIL import Image as Img
from PIL import ImageTk

from GUI.Object import Object
from GUI.Point import Point


class Image(Object):
    def __init__(self, window, path, width=100, height=100, center=Point(0, 0)):
        super().__init__(window, width, center)
        
        self._data = ImageTk.PhotoImage(Img.open(path).resize((width, height)))
        self._id = self._window.canvas.create_image(center.x, center.y, image=self._data)
        self._window.canvas.tag_raise(self._id)
        
        self._path = path
        
    def delete(self):
        del self._data
        self._window.canvas.delete(self._id)