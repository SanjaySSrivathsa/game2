from turtle import Turtle, Screen
import time

position1 = [(0, 0), (-20, 0), (-40, 0)]
move_distance = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
head_check = 0
constant = 1
c = 0


class Snake:
    def __init__(self):

        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in position1:
            print(i)
            if i == (0,0):
                self.AddSegemnt(i, 0)
            else:
                self.AddSegemnt(i, 1)


    def AddSegemnt(self, i, head_check):
        if head_check == 0:
            my_turtle = Turtle("square")
            my_turtle.color("yellow")
        else:
            my_turtle = Turtle("square")
            my_turtle.color("white")
        head_check += 1
        my_turtle.penup()
        my_turtle.goto(i)
        self.segments.append(my_turtle)

    def extend_snake(self):
        self.AddSegemnt(self.segments[-1].position(), constant)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            x = self.segments[i - 1].xcor()
            y = self.segments[i - 1].ycor()
            self.segments[i].goto(x, y)
        self.head.forward(move_distance)

    def check_edges(self):
        x1 = self.head.xcor()
        y1 = self.head.ycor()
        if x1 >= 380:
            self.head.goto(-380, y1)
        elif x1 <= -380:
            self.head.goto(380, y1)
        elif y1 >= 360:
            self.head.goto(x1, -360)
        elif y1 <= -360:
            self.head.goto(x1, 360)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
