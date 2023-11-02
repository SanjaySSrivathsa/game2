from turtle import Turtle
ALIGN = "center"
FONT=("Times New Roman", 28, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.count_score = 0
        self.penup()
        self.goto(0, 280)
        self.color("white")
        self.scoreboard()
        self.hideturtle()

    def scoreboard(self):
        self.write(f"Score : {self.count_score}", align=ALIGN, font=FONT)
    def IncreaseScore(self):
        self.count_score+=1
        self.clear()
        self.scoreboard()
    def gameover(self):
        self.goto(0,0)
        self.write("GAME OVER!", align=ALIGN, font=FONT)