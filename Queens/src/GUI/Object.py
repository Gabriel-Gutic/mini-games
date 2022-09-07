from GUI.Point import Point


class Object:
    def __init__(self, window, width=100, center=Point(0, 0)):
        self._id = None
        self._window = window
        self._center = center
        self._width = width
        
    def set_visible(self, visible):
        if visible:
            self._window.canvas.itemconfigure(self._id, state='normal')
        else:
            self._window.canvas.itemconfigure(self._id, state='hidden')
    
    def move(self, center):
        self._window.canvas.move(self._id, center.x - self._center.x, center.y - self._center.y)
        self._center = center
     
    @property
    def center(self):
        return self._center
    
    @center.setter
    def center(self, center):
        self.move(center)
    
    @property
    def width(self):
        return self._width