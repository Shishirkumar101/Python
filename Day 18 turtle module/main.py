import turtle
import random
import colorgram

turtle.colormode(255)
timmy = turtle.Turtle()
timmy.shape('turtle')

timmy.color('red','green')

# Drow Squar
# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)


# Drow Dash line
# for i in range(25):
    # timmy.pendown()
    # timmy.forward(5)
    # timmy.penup()
    # timmy.forward(5)

# Drow Shapes with different number of sides
# color = ['red','green','blue', 'purple', 'yellow', 'black', 'pink','coral']
# for i in range(3,11):
#     timmy.color(color[i-3])
#     for _ in range(i):
#         timmy.forward(100)
#         timmy.right(360/i)



def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)


# move in random direction
#color = ['red','green','blue', 'purple', 'yellow', 'black', 'pink','coral']
# timmy.pensize(5)
# timmy.speed('fastest')
# for _ in range(50):
    # timmy.color(random_color()) 
    # timmy.forward(25)
    # timmy.setheading(random.choice([0,90,180,270]))

# Drow spirograph
# timmy.speed('fastest')
# def drow_spirograph(size_of_gap):
#     for _ in range(360//size_of_gap):
#         timmy.color(random_color())
#         timmy.circle(100)
#         timmy.setheading(timmy.heading()+size_of_gap)

# drow_spirograph(5)


colors = colorgram.extract('hirest.jpg', 20)
rgb_color = []
for color in colors:
    new_color = (color.rgb.r, color.rgb.g, color.rgb.b)
    rgb_color.append(new_color)
print(rgb_color)

timmy.hideturtle()
timmy.setheading(225)
timmy.penup()
timmy.forward(250)
timmy.setheading(0)

for _ in range(10):
    current = timmy.pos()
    for _ in range(10):
        timmy.dot(20,random.choice(rgb_color))
        timmy.forward(25)
    timmy.teleport(current[0],current[1]+25)

screen = turtle.Screen()    
screen.exitonclick()