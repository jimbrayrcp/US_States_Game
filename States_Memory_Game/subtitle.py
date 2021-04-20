# ################################
#   Copyright (c) 2021 Jim Bray
#       All Rights Reserved
# ################################
from turtle import Turtle

FONT = ("arial", 20, "normal")
ALIGN = "center"


class Subtitle(Turtle):
    def __init__(self):
        super(Subtitle, self).__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("black")
        self.setposition(0, -320)
        self.speed(0)
        self.update_subtitle()

    def update_subtitle(self):
        self.clear()
        text = f"Type `Exit` into the text field when you can't remember any \n" \
               f"others, A study list will will be available for you to save"
        self.write(text, move=False, align=ALIGN, font=FONT)


if __name__ == "__main__":
    from turtle import Turtle, Screen

    turtle = Turtle()
    screen = Screen()
    screen.title("U.S. States Game")
    image = "blank_states_img.gif"
    screen.addshape(image)
    turtle.shape(image)

    x_pos = -38
    y_pos = -106
    state_text = "Texas"
    subtitle = Subtitle()
    screen.mainloop()
