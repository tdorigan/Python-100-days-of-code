from turtle import Turtle

# snake starting size
STARTING_SIZE = 3
# size of the square
MOVE_DISTANCE = 20
# absolute angle positions
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        # attribute specific for the head (segment[0]) because it'll be used many times around the code
        self.head = self.segments[0]

    def create_snake(self):
        """Create a snake with 3 segments"""
        xcor = 0
        for _ in range(STARTING_SIZE):
            xcor -= MOVE_DISTANCE
            position = (xcor, 0)
            self.add_segment(position)

    def add_segment(self, position):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(position[0], position[1])
        self.segments.append(segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def reset(self):
        for segment in self.segments:
            segment.hideturtle()
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def move(self):

        """Move the snake forward 20"""
        # iterates from the last position backwards until 1 (position 0 will be managed outside the for loop)
        for index in range(len(self.segments) - 1, 0, -1):
            # gets the position of the next segment
            position_next = self.segments[index - 1].position()

            # current segment gets the position of the next segment
            self.segments[index].goto(position_next[0], position_next[1])

        # the first position, snake head
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if not self.head.heading() == DOWN:
            self.head.setheading(UP)

    def down(self):
        if not self.head.heading() == UP:
            self.head.setheading(DOWN)

    def left(self):
        if not self.head.heading() == RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if not self.head.heading() == LEFT:
            self.head.setheading(RIGHT)
