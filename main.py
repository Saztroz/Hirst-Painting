import turtle as turtle_module
import random

color_list = [(134, 164, 201), (223, 151, 102), (30, 43, 62), (200, 136, 148), (161, 61, 50), (235, 212, 90), (47, 101, 143), (137, 181, 161), (149, 63, 71), (157, 32, 28), (168, 29, 33), (55, 47, 45), (52, 40, 43), (60, 114, 98), (230, 163, 168), (214, 83, 73), (237, 166, 156), (35, 60, 54), (15, 96, 70), (33, 61, 106), (192, 99, 108), (171, 188, 220), (107, 125, 160), 
(18, 83, 104), (174, 200, 190), (36, 150, 208)]
tim = turtle_module.Turtle()
tim.speed("fastest")
turtle_module.colormode(255)

tim.penup()
tim.hideturtle()

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots+1):
    tim.pendown()
    tim.dot(20, random.choice(color_list))
    tim.penup()
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()