from turtle import Screen

#If I want the snake to show uo on the screen
#I have to first import the snake class from the snake file and then create a new snake object
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

#time help me to reduce the time between a for
import time

#Set up the screen
screen = Screen()
screen.setup(width=600, height=600)

# Change the background color
screen.bgcolor("black")

# Set up a title of the window that shows up
screen.title("My Snake Game")

# Turn off the tracer(n=None, delay=None) -- The tracer is a method in the screen class. we are going to set it to zero
screen.tracer(0)

"""Create the snake object --->
    one the line gets triggered, then we're going to be calling create_snake() and the 3 
    segments will show up on the screen """
snake = Snake()

#Create the object food from Food class
food = Food()

#Create the object scoreboard from the class ScoreBoard
scoreboard = ScoreBoard()
# Set the screen to listen< ^ >
screen.listen()
# to control the turtle with the keyboard
screen.onkey(fun = snake.up,key="Up")
screen.onkey(fun = snake.down,key="Down")
screen.onkey(fun = snake.left,key="Left")
screen.onkey(fun = snake.right, key="Right")




# if we want something to continuously happy in our program, we use while
game_is_on = True
while game_is_on:
    screen.update()  # --> it could be here
    time.sleep(0.1) #---> it deletes 0,1

    snake.move()

    #Detect collision with food #Using .distance method
    if snake.head.distance(food) < 15:
        print("nom nom nom")
        food.refresh()
        snake.extend()
        scoreboard.increase_score()


    #Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() <-280:
        scoreboard.reset()
        snake.reset()


    #Detect collision with tail.

    #for segment in snake.segments[1:]:
    #     if segment == snake.head:  #Otherwise would be game over when it stars
    #         pass----> this is wihout using slicing
    #list_without_head = snake.segments[1:]
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) <10:
            scoreboard.reset()
            snake.reset()


    #if head collides with any segment in the tail:
        #trigger_game_over

screen.exitonclick()
