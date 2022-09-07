from GUI.Point import Point
from GUI.Object import Object
from GUI import Color


class Rectangle(Object):
    def __init__(self, window, width=200, height=100, center=Point(0, 0), color=Color.White):
        super().__init__(window, width, center)
        
        self._height = height
        
        w = width // 2
        h = height // 2
        self._id = self._window.canvas.create_rectangle(
                                           self._center.x - w, 
                                           self._center.y - h, 
                                           self._center.x + w, 
                                           self._center.y + h, 
                                           fill=color)
        