from turtle import Turtle,Screen
import random

screen = Screen()
is_race_on = False
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color: ")
colors = ["red","orange","yellow","green","blue","purple"]
y_positions = [-70,-40,-10,20,50,80]
all_turtles = []

for turtles in range(0,6):
    tim = Turtle(shape="turtle")
    tim.color(colors[turtles])
    tim.penup()
    tim.goto(x=-230,y=y_positions[turtles])
    all_turtles.append(tim)

if user_bet:
    is_race_on = True;


while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"Congratulations you have won. The {winning_color} is the winner")
            else:
                 print(f"You have lost. The {winning_color} is the winner")


        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)


screen.exitonclick()
