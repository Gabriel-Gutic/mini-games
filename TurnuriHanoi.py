import tkinter as tk
import time
import threading

window = tk.Tk()

window.resizable(False, False)

WIDTH = 800
HEIGHT = 600

canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

N = 3
DELAY = 50

h = 20
w = 200

class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        
    def __str__(self) -> str:
        return "(" + str(self.x) + ", " + str(self.y) + ")"
    x = 0
    y = 0

def create_rectangle(x, y, width, text, color='black'):
    h1 = h//2
    w1 = width//2
    return {
            'center': Point(x, y),
            'rect': canvas.create_rectangle(x - w1, y - h1, x + w1, y + h1, fill=color),
            'text': canvas.create_text((x, y), text=text, fill='white'), 
        }

platforms = {}
v = ['A', 'C', 'B']

for i in range(1, 4):
    space = 50
    x = i * space + (2 * i - 1) * (w//2)
    y = HEIGHT - h//2
    platforms[v[i - 1]] = create_rectangle(x, y, w, v[i - 1], color='blue')
    platforms[v[i - 1]]["stack"] = []

def rectangle_color(rect, color):
    canvas.itemconfig(rect, fill=color)

def reset():
    for key, p in platforms.items():
        for el in p['stack']:
            canvas.delete(el['rect'])
            canvas.delete(el['text'])
        p['stack'].clear()
    for i in range(1, N + 1):
        center = platforms['A']['center']
        platforms['A']['stack'].append(create_rectangle(center.x, 
                                                        center.y - h * i, 
                                                        width=w - 8 * i, 
                                                        text=str(i), 
                                                        color='black'))

def move(a, b):
    if len(a['stack']) <= 0:
        return
    canvas.itemconfigure(a['stack'][-1]['rect'], fill='red')
    time.sleep(DELAY / 100)
    
    a_center = a['stack'][-1]['center']
    if len(b['stack']) > 0:
        b_center = b['stack'][-1]['center']
    else:
        b_center = b['center']
    
    b['stack'].append(a['stack'][-1])
    b['stack'][-1]['center'] = Point(b_center.x, b_center.y - 20)

    canvas.move(a['stack'][-1]['rect'], b_center.x - a_center.x, b_center.y - 20 - a_center.y)
    canvas.move(a['stack'][-1]['text'], b_center.x - a_center.x, b_center.y - 20 - a_center.y)
    
    print(str(canvas.itemcget(a['text'], 'text')) + " -> " + str(canvas.itemcget(b['text'], 'text')))
    if len(a['stack']) > 0:
        a['stack'].pop()
    time.sleep(DELAY / 100)
    
    if len(b['stack']) <= 0:
        return
    canvas.itemconfigure(b['stack'][-1]['rect'], fill='black')

thread_stoped = False

def hanoi(n, a, b, c):
    global thread_stoped
    if thread_stoped is True:
        print("Thread allready stoped!")
        return
    if n == 1:
        move(a, b)
    else:
        hanoi(n - 1, a, c, b)
        move(a, b)
        hanoi(n - 1, c, b, a)

def start():
    reset()
    hanoi(N, platforms['A'], platforms['B'], platforms['C'])
    button['state'] = tk.NORMAL;

t1 = False

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

scale_number = tk.Scale(window, from_=2, to=10, orient=tk.HORIZONTAL, command=scale_number_event)
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

window.mainloop()

thread_stoped = True
time.sleep(0.5)