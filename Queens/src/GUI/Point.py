

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, P):
        return Point(self.x + P.x, self.y + P.y)
    
    def __mul__(self, x : float):
        return Point(self.x * x, self.y * x)
    
    def __rmul__(self, x : float):
        return Point(self.x * x, self.y * x)
    
    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)
    

