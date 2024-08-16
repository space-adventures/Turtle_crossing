from turtle import Turtle, Screen

FONT = ("Courier", 24, "normal")
score = 0
screen = Screen()


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.color('white')
        self.ht()
        self.goto(-260, 260)
        self.num = 0

    def renew(self):
        self.clear()
        self.write(f"Score: {self.num}", align='left', font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER LOSER", align='center', font=FONT)
