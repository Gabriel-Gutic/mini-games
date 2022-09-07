import random
from time import sleep
import tkinter as tk
import threading


window = tk.Tk("QuickSort")
window.resizable(False, False)

WIDTH = 800
HEIGHT = 600

DELAY = 100

canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

def pause():
    sleep(DELAY / 100)

def swap_squares(s1, s2, t1, t2):
    square_color(s1, color="green")
    square_color(s2, color="green")
    
    pause()
    
    square_text(s1, t2)
    square_text(s2, t1)
    
    pause()
    
    square_color(s1, color="black")
    square_color(s2, color="black")
    
    

def partition(x, left, right):
    c1 = squares[left]['center']
    c2 = squares[right]['center']
    
    arrow_squares = []
    arrow_squares.append(create_square(c1.x, c1.y - 70, 50, text="\\/", color="red"))
    arrow_squares.append(create_square(c2.x, c2.y - 70, 50, text="\\/", color="red"))
    
    
    i = left + 1
    j = right
    pivot = x[left]
    square_color(squares[left], color="purple")
    pause()
    while True:
        while i <= right and x[i] < pivot:
            square_color(squares[i], color="blue")
            pause()
            square_color(squares[i], color="black")
            i += 1
        if i <= right:
            square_color(squares[i], color="blue")
            pause()
        while j >= left and x[j] > pivot:
            square_color(squares[j], color="blue")
            pause()
            square_color(squares[j], color="black")
            j -= 1
        if j >= left:
            square_color(squares[j], color="blue")
            pause()
        
        if i < j:
            swap_squares(squares[i], squares[j], str(x[i]), str(x[j]))
            x[i], x[j] = x[j], x[i]
        else:
            swap_squares(squares[left], squares[j], str(x[left]), str(x[j]))
            x[left], x[j] = x[j], x[left]
            for square in arrow_squares:
                destroy_square(square)
            arrow_squares.clear()
            square_color(squares[j], color="yellow")
            square_text_color(squares[j], color="black")
            return j
    
def quicksort(x, left, right):
    if left < right:
        s = partition(x, left, right)
        quicksort(x, left, s - 1)
        quicksort(x, s + 1, right)

class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        
    def __str__(self) -> str:
        return "(" + str(self.x) + ", " + str(self.y) + ")"
    x = 0
    y = 0

h = 20

def create_square(x, y, width, text, color='black'):
    w1 = width//2
    return {
            'center': Point(x, y),
            'square': canvas.create_rectangle(x - w1, y - w1, x + w1, y + w1, fill=color),
            'text': canvas.create_text((x, y), text=text, fill='white'), 
        }        

def destroy_square(square):
    canvas.delete(square['square'])
    canvas.delete(square['text'])

def square_color(square, color):
    canvas.itemconfig(square['square'], fill=color)

def square_text(square, text):
    canvas.itemconfig(square['text'], text=text)
    
def square_text_color(square, color):
    canvas.itemconfig(square['text'], fill=color)

N = 10
V = []
squares = []

def start():
    for square in squares:
        destroy_square(square)
    V.clear()
    squares.clear()
    
    W = (800 - (N * 50 + (N - 1) * 20)) // 2 + 25
    
    for i in range(N):
        V.append(random.randint(-100, 100))
        squares.append(create_square(x=W + i * 70, y=300, width=50, text=str(V[i])))
        
    quicksort(V, 0, N - 1)
    for square in squares:
        square_text_color(square, color="black")
        square_color(square, color="orange")
    print(V)
    button['state'] = tk.NORMAL
    

def animation_thread():
    button['state'] = tk.DISABLED;
    t1=threading.Thread(target=start)
    t1.start()

button = tk.Button(window, text="Start", command=animation_thread, anchor=tk.W)
button.configure(width = 20, height=1, bg='gray', fg='black')
button_window = canvas.create_window(50, 20, anchor=tk.NW, window=button)

entry_number_label = canvas.create_text(240, 32, text="Number: ")

def scale_number_event(event):
    global N
    N = scale_number.get()

scale_number = tk.Scale(window, from_=2, to=11, orient=tk.HORIZONTAL, command=scale_number_event)
scale_number.set(N)
scale_number.configure(width = 10, relief = tk.FLAT)
scale_number_window = canvas.create_window(270, 7, anchor=tk.NW, window=scale_number)

entry_delay_label = canvas.create_text(400, 32, text="Delay: ")

def scale_delay_event(event):
    global DELAY
    DELAY = scale_delay.get()

scale_delay = tk.Scale(window, from_=1, to=200, orient=tk.HORIZONTAL, command=scale_delay_event)
scale_delay.set(DELAY)
scale_delay.configure(width = 10, relief = tk.FLAT)
scale_delay_window = canvas.create_window(425, 7, anchor=tk.NW, window=scale_delay)

def create_rectangle(x, y, width, text, color='black'):
    h1 = 40
    w1 = width//2
    return {
            'center': Point(x, y),
            'rect': canvas.create_rectangle(x - w1, y - h1, x + w1, y + h1, fill=color),
            'text': canvas.create_text((x, y), text=text, fill='white'), 
        }

legend = []
legend.append(create_rectangle(150, 400, 200, "Pivot in constructie", color="purple"))
legend.append(create_rectangle(400, 400, 200, "Pivot stabilit", color="yellow"))
canvas.itemconfig(legend[-1]['text'], fill="black")
legend.append(create_rectangle(650, 400, 200, "Elemente interschimbate", color="green"))
legend.append(create_rectangle(275, 500, 200, "Element curent", color="blue"))
legend.append(create_rectangle(525, 500, 200, "Stanga si dreapta", color="red"))

window.mainloop();
