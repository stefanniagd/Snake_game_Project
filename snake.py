from turtle import Turtle

# TODO: I need t create the Snake class-
#       Defining the attributes ( The way that it looks, speed..)
#       and then the methods (The things that the snake does)
#       before I need to put as a constant the starting point of the snake in Uppercase


STARTING_POSITIONS= [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20    # If we want to change something gets easier when I set this as constant
RIGHT = 0
UP = 90
LEFT =180
DOWN =270

class Snake:
    def __init__(self):  # What should happen when we initialize a new snake object
        #Attribute
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self): # I'm creating a method and inside I need to use
        for position in STARTING_POSITIONS:
            self.add_segment(position)


    def add_segment(self,position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        for seg in self.segments:  # I sent the segments to a position that is outside the screen's size
            seg.goto(1000,100)
        self.segments.clear() # It removes all the items of  the list of segments
        self.create_snake()
        self.head = self.segments[0] # Basically we are doing everything that is inside the init

    def extend(self):
        #add a new segment to the snake.
        self.add_segment(self.segments[-1].position())




    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num  - 1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)



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










