from turtle import Turtle,Screen
import random
is_race_on = False
s = Screen()
s.bgcolor("light green")
s.setup(500,400)
user_bet = s.textinput(title="Make your bet",prompt="Which Turtle will win the race? Enter a color: ")
color = ["red","orange","yellow","green","blue","purple"]
y_position = [-70,-40,-10,20,50,80]
all_t  = []
for tim_index in range(0,6):
    t = Turtle(shape="turtle")
    t.color("black",color[tim_index])
    t.penup()
    t.goto(x=-230, y=y_position[tim_index])
    all_t.append(t)


if user_bet:
    is_race_on = True


while is_race_on:
    for tu in all_t:
        if tu.xcor() > 230:
            winning = tu.fillcolor()
            if winning == user_bet:
                print(f"You've won! The  {winning} turtle is the winner!")
                is_race_on = False
            else:
                print(f"You've lost! The  {winning} turtle is the winner!")
                is_race_on = False
        random_dis = random.randint(0,10)
        tu.forward(random_dis)
s.exitonclick()