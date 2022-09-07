from time import sleep
import os
import threading

from GUI.Window import Window
from GUI.Point import Point
from GUI.Slider import Slider
from GUI.Image import Image
from GUI.Button import Button
from GUI.Label import Label
from Table import Table


location = os.path.dirname(os.path.realpath(__file__))
os.chdir(location)


window = Window("Queen", 800, 600)

table = Table(window, 5, center=Point(400, 300))
queens = []
DELAY = 1000

def pause():
    sleep(DELAY / 1000)


def slider_rows_func(n):
    global table
    table.delete()
    table = Table(window, int(n), center=Point(400, 300))


slider_rows = Slider(window, start=2, end=15,
                   command=slider_rows_func,
                   width=20,
                   center=Point(350, 30))
slider_rows.set(table.rows)


def valid(k):
    for i in range(k):
        q1 = queens[i]['col']
        q2 = queens[k]['col']
        if q1 == q2 or (abs(k - i) == abs(q2 - q1)):
            return False
    return True


def solution(k):
    return k == table.rows - 1


def show_solution():
    w = table.squares[0][0].width
    for i in range(len(queens)):
        queens[i]['image'].delete()
        queens[i]['image'] = Image(window, width=w, height=w,
                           center=table.squares[i][queens[i]['col']].center,
                           path="../images/queen_green.png")
    pause()
    for i in range(len(queens)):
        queens[i]['image'].delete()
        queens[i]['image'] = Image(window, width=w, height=w, 
                           center=table.squares[i][queens[i]['col']].center,
                           path="../images/queen.png")
    pause()


is_running = True


def back(k):
    for i in range(table.rows):
        global is_running
        if not is_running:
            return False
        queens[k]['col'] = i
        queens[k]['image'].center = table.squares[k][i].center
        queens[k]['image'].set_visible(True)
        pause()
        if valid(k):
            if solution(k):
                show_solution()
            else:
                back(k + 1)
    queens[k]['image'].set_visible(False)
    pause()


def backtracking_init():
    back(0)
    reset()
 

def start():
    slider_rows.set_visible(False)
    start_button.set_visible(False)
    w = table.squares[0][0].width
    for i in range(table.rows):
        queens.append({
        'col': None,
        'image': Image(window, width=w, height=w, path="../images/queen.png"),
        })
        queens[i]['image'].set_visible(False)
    
    backtracking_thread = threading.Thread(target=backtracking_init)
    backtracking_thread.start()


start_button = Button(window, command=start, 
                            text='Start', center=Point(400, 550))


def reset():
    is_running = False
    for queen in queens:
        queen['image'].delete()
    queens.clear()
    start_button.set_visible(True)
    slider_rows.set_visible(True)


reset_button = Button(window, command=reset, 
                            text='Reset', center=Point(100, 550))


def slider_delay_event(event):
    global DELAY
    DELAY = int(event)


delay_text = Label(window, "Delay: ", Point(40, 478), font_size=14)
slider_delay = Slider(window, start=1, end=2000,
                   command=slider_delay_event,
                   width=20,
                   center=Point(70, 450))
slider_delay.set(1000)


window.run()