from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.scorevalue = 0
        self.speed(0)
        self.penup()
        self.color("white")
        self.goto(x=0, y=265)
        self.hideturtle()
        self.updatescore()

    def updatescore(self):
        self.clear()
        self.write(arg=f"Score = {self.scorevalue}", align=ALIGNMENT, font=FONT)

    def gameover(self):
        self.goto(x=0, y=0)
        self.write(arg="GAME OVER!", align=ALIGNMENT, font=FONT)

    def increasescore(self):
        self.scorevalue += 1
        self.updatescore()
