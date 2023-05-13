from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.scorevalue = 0
        self.highscore = 0
        self.speed(0)
        self.penup()
        self.color("white")
        self.goto(x=0, y=265)
        self.hideturtle()
        self.updatescore()

    def updatescore(self):
        self.clear()
        self.write(arg=f"Score = {self.scorevalue} High Score = {self.highscore}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.scorevalue > self.highscore:
            self.highscore = self.scorevalue
        self.scorevalue = 0
        self.updatescore()

    def increasescore(self):
        self.scorevalue += 1
        self.updatescore()
