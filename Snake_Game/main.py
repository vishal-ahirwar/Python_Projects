# ©2021 Vishal Ahirwar. 
from turtle import Screen
from random import choice
import turtle
from snake import Snake
from food import Food
from ui import ScoreBoard
from end_ui import EndUI
import time

screen = Screen()
screen.setup(850, 650)
colors =["blue","white","green","red","yellow","pink"]


def Quit():
    Q_ui = EndUI()
    Q_ui.Last_Message()
    screen.exitonclick()


def Snake_Loop():
    screen.clear()
    turtle.clear()
    screen.title(
        "My Snake Game v.01. ©2021 Vishal Ahirwar. All rights reserved. ")
    screen.bgcolor("black")
    screen.tracer(0)
    snake = Snake("square", choice(colors))
    food = Food(choice(colors))
    Score = ScoreBoard()

    Game_Is_On = True
    while Game_Is_On:
        screen.update()
        time.sleep(0.1)
        snake.Move()

        if snake.Snake_head.distance(food) < 15:
            print("non non non")
            snake.IncreaseSnackeSize()
            food.Refresh()
            Score.Refresh()

        if snake.IsDead():
            Game_Is_On = False
            Score.Game_Over()

            screen.listen()
            screen.onkey(Quit, "q")
            screen.onkey(Snake_Loop, "r")


Snake_Loop()
screen.exitonclick()
