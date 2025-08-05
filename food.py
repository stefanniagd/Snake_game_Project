from turtle import Turtle
import random
"""how to render itself as a small circle on the screen- Everytime that the snake touches the
food it is going to move to a random location
The class Food to inherit from the turtle class- So that way this food class is going to have
all the capabilities of the turtle class but it's algo going to have some specific things that we are going to tell it
how to do so that it behaves like an actual piece of food
"""

class Food(Turtle): #Turtle Superclass

    def __init__(self):
        super().__init__()
        self.shape("circle")#This come from the turtle superclass
        self.penup()#This come from the turtle superclass
        self.shapesize(stretch_len=0.5,stretch_wid= 0.5)  # I'm able to use it because I'm inheriting from the Turtle
        self.color("yellow")
        self.speed("fastest")
        self.refresh()
        # All of this is going to happen as soon as I create a new object from the food class

    def refresh(self):
        random_x = random.randint(-280,280)
        random_y =random.randint(-280,280)
        self.goto(random_x, random_y)


