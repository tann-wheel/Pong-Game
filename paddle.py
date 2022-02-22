from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()

        self.goto(position)

    def pong_up(self):
        changed_y = self.ycor() + 20
        self.goto(self.xcor(), changed_y)

    def pong_down(self):
        changed_y = self.ycor() -20
        self.goto(self.xcor(), changed_y)





