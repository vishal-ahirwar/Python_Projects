# ©2021 Vishal Ahirwar. 
from turtle import Turtle
class EndUI(Turtle):
    def __init__(self):
        super().__init__();
        self.color("red")
        self.hideturtle();
        self.penup();

    
    def Last_Message(self):
        self.goto(0,-250);
        self.write("Click AnyWhere on the Game Window to Quit or Press R to Restart Game.",align="center",font=("Arial",15,"normal"));

