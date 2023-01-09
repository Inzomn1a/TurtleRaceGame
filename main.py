import turtle
from turtle import Turtle, Screen
import random

# Initial Setup

screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "orange", "black", "blue", "green", "purple"]
turtle_names = ["jim", "tim", "kim", "john", "tron", "ron"]

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?\nRed, Orange, Black, Blue, Green, Purple").upper()


race_is_on = False
iterator = 0
y_offset = -50
all_turtles = []
for name in turtle_names:
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[iterator])
    new_turtle.setposition(-230, y_offset)
    all_turtles.append(new_turtle)
    iterator += 1
    y_offset += 25

if user_bet:
    race_is_on = True

while race_is_on:
    for turtle in all_turtles:
        if turtle.xcor() < 220:
            turtle.pendown()
            random_turtle_distance = random.randrange(1, 20)
            turtle.forward(random_turtle_distance)
        else:
            race_is_on = False
            print(f"The {turtle.pencolor().upper()} Turtle has won.")
            if turtle.pencolor().upper() == user_bet:
                print("You won the bet.")
            else:
                print("You've lost the bet.")


screen.exitonclick()
