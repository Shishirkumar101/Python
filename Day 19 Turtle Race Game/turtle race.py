from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500 , height=400)
is_game_started = False
user_bet = screen.textinput(title="Enter your bet", prompt="which turtle will win the race? Enter a color: ")
colors = ['red','green','blue','yellow','orange', 'purple']
y_positions = [-70,-40,-10,20,50,80]
all_turtles = []
for i in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(-230,y_positions[i])
    all_turtles.append(new_turtle)

if user_bet:
    is_game_started = True
while(is_game_started):
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_game_started = False
            if turtle.pencolor() == user_bet:
                print(f"You've won! {turtle.pencolor()} turtle is the winner!")
            else:
                print(f"You've lose! {turtle.pencolor()} turtle is the winner!")
        else:
            turtle.forward(random.randint(0,10))
