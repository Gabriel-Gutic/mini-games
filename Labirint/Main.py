from re import X
import tkinter as tk

from Point import Point
from Square import Square
from Maze import Maze


window = tk.Tk("Soarecele prin labirint")

window.resizable(False, False)

WIDTH = 800
HEIGHT = 600

canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

s = Square(canvas, Point(400, 300), 50, "Hello", border="red")
s.move(Point(100, 100))

maze = Maze(canvas, Point(400, 300), 10, 9, 500)

def comm():
    maze.set_cols(15)

button = tk.Button(window, text="Start", command=comm, anchor=tk.W)
button.configure(width = 20, height=1, bg='gray', fg='black')
button_window = canvas.create_window(50, 20, anchor=tk.NW, window=button)

window.mainloop()