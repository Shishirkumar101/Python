import turtle
import pandas


def write_state_name(a,b,state):
    print(a,b)
    state_name = turtle.Turtle()
    state_name.penup()
    state_name.hideturtle()
    state_name.goto(a ,b)
    state_name.write(state,align="center")

screen = turtle.Screen()
screen.title("U.S State Game")

image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)
count = 0
data = pandas.read_csv("50_states.csv")
state_list = data["state"].to_list()

is_game_over = True
while is_game_over:
    answer_state = screen.textinput(title=f"{count}/50 Guess the State", prompt="What's another state name? ").title()
    if answer_state ==  "Exit":
        df = pandas.DataFrame(state_list , columns=["state"])
        df.to_csv("remaning_state.csv", index=False)
        break
    if answer_state in state_list:
        count += 1
        state_data = data[data["state"] == answer_state]
        x = int(state_data['x'].item())
        y = int(state_data['y'].item())
        write_state_name(x,y, answer_state)
        state_list.remove(answer_state)
