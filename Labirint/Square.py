

class Square:
    def __init__(self, canvas, center, width, text='', color='black', border=None) -> None:
        w = width // 2
        self.canvas = canvas
        self.center = center
        self.id = canvas.create_rectangle(center.x - w, center.y - w, center.x + w, center.y + w, fill=color, outline=border)
        self.text = canvas.create_text((center.x, center.y), text=text, fill='white')
    
    def delete(self):
        self.canvas.delete(self.id)
        self.canvas.delete(self.text)
    
    def move(self, center):
        self.canvas.move(self.id, center.x - self.center.x, center.y - self.center.y)
        self.canvas.move(self.text, center.x - self.center.x, center.y - self.center.y)
        self.center = center
            
        
        