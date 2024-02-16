# ©2021 Vishal Ahirwar. 
from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self,food_color) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.6, stretch_wid=0.6)
        self.color(food_color)
        self.speed("fastest")
        self.Refresh()

    def Refresh(self):
        x = randint(-250, 250)
        y = randint(-325, 325)
        self.goto(x, y)
