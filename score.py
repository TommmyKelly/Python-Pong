from turtle import (Turtle)
FONT = "Courier"


class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(position)
        self.write(self.score, font=(FONT, 80, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(self.score,  font=(FONT, 80, "normal"))

