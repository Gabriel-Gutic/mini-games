from GUI.Square import Square
from GUI.Point import Point
from GUI.Object import Object


class Table(Object):
    def __init__(self, window, rows, width=400, center=Point(0, 0)):
        super().__init__(window, width, center)
        self._rows = rows
        self._squares = None
        
        self.generate()
    
    def generate(self):
        self._squares = [[None for i in range(self._rows)] for i in range(self._rows)]
        
        width = self._width
        square_width = width // self._rows
        
        q = width // 2 - square_width // 2
        
        for i in range(self._rows):
            for j in range(self._rows):
                x = self._center.x - q + square_width * j
                y = self._center.y - q + square_width * i
                self._squares[i][j] = Square(window=self._window,
                                            center=Point(x, y),
                                            width=square_width,
                                            color='white',
                                            )
                
    def delete(self):
        for i in range(self._rows):
            for j in range(self._rows):
                self._squares[i][j].delete()
        self._squares.clear()
    
    @property
    def rows(self):
        return self._rows
    
    @rows.setter
    def rows(self, m):
        self.delete()
        self._rows = m
        self.generate()
        
    @property
    def squares(self):
        return self._squares