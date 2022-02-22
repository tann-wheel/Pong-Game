from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_new=10
        self.y_new=10
        self.move_speed=0.1


    def move(self):
        new_x=self.xcor()+self.x_new
        new_y=self.ycor()+self.y_new
        self.goto(new_x,new_y)

    def bounce_y(self):
        self.y_new*=-1

    def bounce_x(self):
        self.x_new*=-1
        self.move_speed*=0.9

    def reset_position(self):
        self.goto(0,0)
        self.move_speed=0.1
        self.bounce_x()
