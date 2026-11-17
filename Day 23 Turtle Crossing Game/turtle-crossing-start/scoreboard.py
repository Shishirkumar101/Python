from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(-200,250)
        self.level = 1
        self.color('black')
        self.displaye_score()

    def displaye_score(self):
        self.clear()
        self.write(f"Level : {self.level}" , align='center', font=FONT)

    def update_score(self):
        self.level +=1
        self.displaye_score()


    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align='center', font= FONT)