from turtle import Turtle, Screen

STARTING_POSITION = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
Turtle.position
class Snake():
    def __init__(self):
        self.all_turtle = []
        self.create_snake()
        self.head = self.all_turtle[0]


    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self , position):
        new_turtle = Turtle(shape='square')
        new_turtle.color('white')
        new_turtle.penup()
        new_turtle.goto(position)
        self.all_turtle.append(new_turtle)

    def extend(self):
        self.add_segment(self.all_turtle[-1].position())

    def move(self):
        for i in range(len(self.all_turtle)-1,0,-1):
            new_x = self.all_turtle[i-1].xcor()
            new_y = self.all_turtle[i-1].ycor()
            self.all_turtle[i].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

        # position = self.all_turtle[0].heading()
        # if position == 0:
        #     self.all_turtle[0].left(90)
        # elif position == 180:
        #     self.all_turtle[0].right(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

        # position = self.all_turtle[0].heading()
        # if position == 180:
        #     self.all_turtle[0].left(90)
        # elif position == 0:
        #     self.all_turtle[0].right(90)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        # position = self.all_turtle[0].heading()
        # if position == 270:
        #     self.all_turtle[0].left(90)
        # elif position == 90:
        #     self.all_turtle[0].right(90)   
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        # position = self.all_turtle[0].heading()
        # if position == 90:
        #     self.all_turtle[0].left(90)
        # elif position == 270:
        #     self.all_turtle[0].right(90)