# ################################
#   Copyright (c) 2021 Jim Bray
#       All Rights Reserved
# ################################
import turtle
from time import sleep
from data_worker import States
from subtitle import Subtitle
from turtle_graphics import TextMarker

screen = turtle.Screen()

width, height = screen.window_width(), screen.window_height()
canvas = screen.getcanvas()

left, top = 100, 100
geom = '{}x{}+{}+{}'.format(width, height, left, top)
canvas.master.geometry(geom)

screen.title("U.S. States Game |  0/50 ")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
subtitle = Subtitle()
states = States()
states.new_game_memory()

game_is_on = True
while game_is_on:
    screen.update()
    sleep(0.1)
    # ADD TEXT TO SCREEN
    score = states.last_score()
    answer = screen.textinput(title=f"Guess a State | {score}/50 ", prompt=" What's another state's name?\n")

    # BREAK OUT ON EXIT
    if answer.title() == "Exit":
        states.states_to_learn()
        states.open_states_to_learn()
        break

    # COMPARE DATA TO ANSWER
    state_returned = states.check_state(answer)
    if state_returned:
        print(f"RETURNED: {state_returned[0]} {state_returned[1]} {state_returned[2]}")
        text_marker = TextMarker()
        text_marker.set_new_text(pos_x=state_returned[0], pos_y=state_returned[1], state_text=state_returned[2])

    # SET THE SCORE ONTO THE SCREEN
    score = states.last_score()
    set_title = f"U.S. States Game |  {score}/50 "
    screen.title(set_title)
    if score == 50:
        game_is_on = False
