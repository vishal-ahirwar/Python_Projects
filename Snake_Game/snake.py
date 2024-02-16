# ©2021 Vishal Ahirwar. 
from turtle import Turtle, Screen
MOVE_DIST = 20


class Snake():

    def __init__(self, snake_shape, snake_color):
        self.screen = Screen()
        self.Snake_Body = []
        tl = Turtle("circle")
        tl.penup()
        tl.speed("fastest")
        tl.color("red")
        tl.goto(x=0, y=0)
        self.Snake_Body.append(tl)
        self.Create_Snake(snake_shape, snake_color)
        self.Snake_head = self.Snake_Body[0]
        self.screen.listen()
        self.screen.onkey(self.Left, "a")
        self.screen.onkey(self.Right, "d")
        self.screen.onkey(self.Up, "w")
        self.screen.onkey(self.Down, "s")

    def Create_Snake(self, snake_shape, snake_color):
        self.snake_color = snake_color
        self.snake_shape = snake_shape
        for i in range(2):
            self.tl = Turtle(self.snake_shape)
            self.tl.penup()
            self.tl.speed("fastest")
            self.tl.color(self.snake_color)
            self.tl.goto(self.tl.xcor()-(i*20), y=0)
            self.Snake_Body.append(self.tl)

    def IncreaseSnackeSize(self):
        new_snake = Turtle(self.snake_shape)
        new_snake.penup()
        new_snake.speed("fastest")
        new_snake.color(self.snake_color)
        new_snake.goto(self.Snake_Body[-1].position())
        self.Snake_Body.append(new_snake)

    def Left(self):
        self.Snake_head.setheading(180)

    def Right(self):
        self.Snake_head.setheading(0)

    def Up(self):
        self.Snake_head.setheading(90)

    def Down(self):
        self.Snake_head.setheading(-90)

    def Move(self):
        for seg_ in range(len(self.Snake_Body)-1, 0, -1):
            new_x = self.Snake_Body[seg_-1].xcor()
            new_y = self.Snake_Body[seg_-1].ycor()
            self.Snake_Body[seg_].goto(new_x, new_y)
        self.Snake_Body[0].forward(MOVE_DIST)

    def IsDead(self):
        for seg in self.Snake_Body[1:]:
            if self.Snake_head.distance(seg)<10:
                return True
        return self.Snake_head.xcor() > 425 or self.Snake_head.xcor() < -425 or self.Snake_head.ycor() > 325 or self.Snake_head.ycor() < -325
