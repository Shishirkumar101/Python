from turtle import Turtle
FONT = ('Arial', 10, 'normal')
ALIGNMENT = "center"
class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.speed("fastest")
        self.penup()
        self.goto(0,280)
        self.color('white')
        self.score = 0
        self.print_score()

    def print_score(self):
        self.write(f"Score : {self.score}", False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.home()
        self.write(f"GAME OVER", False, align=ALIGNMENT, font=FONT)
    def update_score(self):
        self.score += 1
        self.clear()
        self.print_score()