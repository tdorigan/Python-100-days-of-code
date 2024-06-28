from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        # default size is 20x20. multiplying to 0.5 to get half of the size
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.speed("fastest")

        self.go_to_random_position()

    def go_to_random_position(self):
        random_x = random.randint(-290, 290)
        random_y = random.randint(-290, 290)
        self.goto(random_x, random_y)
