import tkinter as tk
from PIL import Image, ImageTk
import random

window = tk.Tk()

window.resizable(False, False)

canvas = tk.Canvas(window, width=800, height=600)
canvas.grid(columnspan=3, rowspan=10)

ROCK = "Rock"
PAPER = "Paper"
SCISSORS = "Scissors"
ELEMENTS = ["Rock", "Paper", "Scissors"]

level = 1
player_points = 0

round_text = tk.StringVar()
player_choice_text = tk.StringVar()
computer_choice_text = tk.StringVar()
winner_text = tk.StringVar()


def reset():
    global level
    level = 1
    global player_points
    player_points = 0
    round_text.set("Runda: 1")
    player_choice_text.set("")
    computer_choice_text.set("")
    winner_text.set("")


reset()


def level_result(player_choice, computer_choice):
    global level

    player_choice_text.set("Jucatorul a ales: " + player_choice)
    computer_choice_text.set("Computerul a ales: " + computer_choice)
    if player_choice == computer_choice:
        winner_text.set("Este egalitate!")
        return

    if (computer_choice == ROCK and player_choice == PAPER) \
            or (computer_choice == PAPER and player_choice == SCISSORS) \
            or (computer_choice == SCISSORS and player_choice == ROCK):
        # Player won a level
        global player_points
        player_points += 1
        winner_text.set("Jucatorul a castigat runda!")
        if player_points >= 2:
            round_text.set("Felicitari, ati castigat!")
            level = 4
            return
    else:
        winner_text.set("Jucatorul a pierdut runda!")
        if level - player_points >= 2:
            round_text.set("Calculatorul v-a invins(cinstit, nu trisand)")
            level = 4
            return
    level += 1
    round_text.set("Runda: " + str(level))


def random_choice():
    r = random.Random()
    return ELEMENTS[r.randrange(0, 3)]


# BUTTONS
WIDTH_BUTTON = 200


# ROCK BUTTON
def rock_button_event():
    if level < 4:
        if player_points >= 1:  # Computer must win
            level_result(ELEMENTS[0], ELEMENTS[1])
        else:
            level_result(ELEMENTS[0], random_choice())


rock_image = Image.open(r"Cursuri/Curs 1/Teme/Problema4/assets/rock.png")
rock_image = rock_image.resize((WIDTH_BUTTON, WIDTH_BUTTON), Image.ANTIALIAS)
rock_image = ImageTk.PhotoImage(rock_image)

rock_button = tk.Button(window, command=lambda: rock_button_event(), image=rock_image,
                        height=WIDTH_BUTTON,
                        width=WIDTH_BUTTON)
rock_button.grid(column=0, row=0)


# PAPER BUTTON
def paper_button_event():
    if level < 4:
        if player_points >= 1:  # Computer must win
            level_result(ELEMENTS[1], ELEMENTS[2])
        else:
            level_result(ELEMENTS[1], random_choice())


paper_image = Image.open(r"Cursuri/Curs 1/Teme/Problema4/assets/paper.png")
paper_image = paper_image.resize((WIDTH_BUTTON, WIDTH_BUTTON), Image.ANTIALIAS)
paper_image = ImageTk.PhotoImage(paper_image)

paper_button = tk.Button(window, command=lambda: paper_button_event(), image=paper_image,
                         height=WIDTH_BUTTON,
                         width=WIDTH_BUTTON)
paper_button.grid(column=1, row=0)


# SCISSORS BUTTON
def scissors_button_event():
    if level < 4:
        if player_points >= 1: # Computer must win
            level_result(ELEMENTS[2], ELEMENTS[0])
        else:
            level_result(ELEMENTS[2], random_choice())


scissors_image = Image.open(r"Cursuri/Curs 1/Teme/Problema4/assets/scissors.png")
scissors_image = scissors_image.resize((WIDTH_BUTTON, WIDTH_BUTTON), Image.ANTIALIAS)
scissors_image = ImageTk.PhotoImage(scissors_image)

scissors_button = tk.Button(window, command=lambda: scissors_button_event(), image=scissors_image,
                            height=WIDTH_BUTTON,
                            width=WIDTH_BUTTON)
scissors_button.grid(column=2, row=0)

# ROUND
round_label = tk.Label(window, textvariable=round_text, font=("Simple", 20), fg='Black')
round_label.grid(columnspan=3, column=0, row=3)

round_text.set("Runda: 1")

# PLAYER CHOICE
player_choice = tk.Label(window, textvariable=player_choice_text, font=("Simple", 20), fg='Red')
player_choice.grid(columnspan=3, column=0, row=4)

player_choice_text.set("Salut")

# COMPUTER CHOICE
computer_choice = tk.Label(window, textvariable=computer_choice_text, font=("Simple", 20), fg='Blue')
computer_choice.grid(columnspan=3, column=0, row=5)

computer_choice_text.set("Salut")

# WINNER
winner_choice = tk.Label(window, textvariable=winner_text, font=("Simple", 20), fg='Green')
winner_choice.grid(columnspan=3, column=0, row=6)

winner_text.set("Salut")

# RESET BUTTON
reset_button = tk.Button(window, text="Reset", font=("Simple", 20), command=lambda: reset(),
                         height=2,
                         width=6)
reset_button.grid(column=1, row=7)

window.mainloop()

