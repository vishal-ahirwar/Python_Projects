# ©2021 Vishal Ahirwar. 

from turtle import Turtle, update


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.Score = 0

        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.Update_Text()
        self.hideturtle()

    def Update_Text(self):
        self.write(f"Score : {self.Score}", align="center",
                   font=("Arial", 25, "normal"))


    def Refresh(self):
        self.clear()
        self.Score += 1
        self.Update_Text()

    def Game_Over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Arial", 45, "normal"))
        self.goto(0, self.ycor()-45)
        self.write("Press R to Restart or Q to Quit Game",
                   align="center", font=("Arial", 15, "normal"))
        self.goto(0, self.ycor()-35)
        self.write("Developer : Vishal Ahirwar",
                   align="center", font=("Arial", 15, "normal"))
        self.goto(0, self.ycor()-35)
        self.write("©2021 MySnakeGame Vishal Ahirwar. All rights reserved. ",
                   align="center", font=("Arial", 15, "normal"))
