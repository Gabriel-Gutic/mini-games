from Square import Square
from Point import Point


class Maze:
    def __init__(self, canvas, center, m, n, width):
        self.canvas = canvas
        self.center = center
        self.width = width
        self.rows = m
        self.cols = n
        self.squares = None
        
        self.generate()
    
    def generate(self):
        self.squares = [[None for j in range(self.cols)] for i in range(self.rows)]
        square_width = self.width // self.cols
        height = square_width * self.rows
        q1 = self.width // 2 - square_width // 2
        q2 = height // 2 - square_width // 2
        
        for i in range(self.rows):
            for j in range(self.cols):
                self.squares[i][j] = Square(canvas=self.canvas,
                                            center=Point(self.center.x - q1 + square_width * j,
                                                         self.center.y - q2 + square_width * i),
                                            width=square_width,
                                            color='white',
                                            border='black',
                                            )
    
    def delete(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.squares[i][j].delete()
        self.squares.clear()
                
    def set_rows(self, m):
        self.delete()
        self.rows = m
        self.generate()
        
    def set_cols(self, n):
        self.delete()
        self.cols = n
        self.generate()
        