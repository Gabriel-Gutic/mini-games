from GUI.Object import Object
from GUI.Point import Point
from GUI import Color

class Square(Object):
    def __init__(self, window, width=100, center=Point(0, 0), color=Color.White):
        super().__init__(window, width, center)
        
        w = width // 2
        self._id = self._window.canvas.create_rectangle(self._center.x - w, 
                                           self._center.y - w, 
                                           self._center.x + w, 
                                           self._center.y + w, 
                                           fill=color)
        
    def delete(self):
        self._window.canvas.delete(self._id)
        #self._canvas.delete(self._text_id)