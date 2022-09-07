from GUI.Point import Point


class Label:
    def __init__(self, window, text, center=Point(0, 0), font_size=14):
        self._window = window
        self._center = center
        self._text = text
        self._font_size = font_size
        
        self._id = self._window.canvas.create_text(self._center.x, self._center.y,
                                            text=self._text,
                                            font=('Helvetica',str(self._font_size),'bold'))
    
    @property
    def text(self):
        return self._text
    
    @text.setter
    def text(self, text):
        self._text = text
        self._window.canvas.delete(self._id)
        self._id = self._window.canvas.create_text(self._center.x, self._center.y,
                                            text=self._text,
                                            font=('Helvetica',str(self._font_size),'bold'))

    
    def set_visible(self, visible):
        if visible:
            self._window.canvas.itemconfigure(self._id, state='normal')
        else:
            self._window.canvas.itemconfigure(self._id, state='hidden')
            
    def is_visible(self):
        return self._window.canvas.itemcget(self._id, 'state') == 'normal'
        
        