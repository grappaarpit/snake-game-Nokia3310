from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.starting_positions = [(0, 0), (-20, 0), (-40, 0)]
        self.segments = []

        for positions in self.starting_positions:
            self.add_segment(positions)


    def add_segment(self,positions):
        self.new_segment = Turtle("square")
        self.new_segment.color("white")
        self.new_segment.penup()
        self.new_segment.speed("fastest")
        self.new_segment.goto(positions)
        self.segments.append(self.new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self, distance):

        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.segments[0].forward(distance)

    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)
