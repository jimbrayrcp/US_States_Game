# ################################
#   Copyright (c) 2021 Jim Bray
#       All Rights Reserved
# ################################
from turtle import Turtle

FONT = ("courier", 10, "normal")
ALIGN = "center"


class TextMarker(Turtle):
    def __init__(self):
        super(TextMarker, self).__init__()
        self.score = 0
        self.text_state = ""
        self.y_pos = 0
        self.x_pos = 0
        self.penup()
        self.hideturtle()

    def set_new_text(self, pos_x, pos_y, state_text):
        self.text_state = state_text
        self.y_pos = pos_y
        self.x_pos = pos_x
        self.setposition(self.x_pos, self.y_pos)
        text = f"{self.text_state}"
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
    text_state = "Texas"
    text_marker = TextMarker()
    text_marker.set_new_text(pos_x=x_pos, pos_y=y_pos, state_text=text_state)

    screen.mainloop()
