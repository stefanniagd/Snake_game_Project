from turtle import Screen, Turtle
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
# Turn turtle animation on/off and set delay for update drawings.
# I need to call update in order to refresh the screen
screen.tracer(0)

# TODO: create snake body by creating three squares which are each going to be turtles
#       they are going to be lined up next to each other, to bear in mind the turtle square is 20 pixels x 20

# Empty list for the objets
all_squares = []
#             0           1        2   --->check range I want to go from 2-1-0
x_position = [(0,0), (-20,0), (-40,0)]
color=["red","yellow","orange"]

for square in range(0,3):
    new_square = Turtle(shape ="square")
    new_square.color(color[square])
    new_square.penup()
    new_square.goto(x_position[square])
    print(new_square.position())
    all_squares.append(new_square)

# Call update-- as soon as I open the program the snake appeears but it does not move
#screen.update()

# TODO: move the snake automatically across the screen without having to do anything
#       all we have to do is to change the direction

# if we want something to continuously happy in our program, we use while
game_is_on = True

while game_is_on:
    screen.update()  # --> it could be here
    time.sleep(0.1) #---> it deletes the for loop for 0.1 secs
    for squares_num in range(len(all_squares)-1, 0, -1):   # 1,2,3 (star= 1, stop= 3, step =+1)-- 3,2,1 (star=3, stop=1, step=-1) #(  # reverse order
        new_x = all_squares[squares_num-1].xcor() # new_x = all_squares[3-1].xcor() -- it gives me the x position of 2 square
        new_y =  all_squares[squares_num-1].ycor()# new_y = all_squares[3-1].ycor() -- it gives me the y position of 2 square
        all_squares[squares_num].goto(new_x,new_y) #all_squares[3].goto(x_2position, y_2position) - my squares 3 is going to go to the position of square 2
        print(f"this is square index {squares_num}") # The index 0 is not taking into account because it stops at 0
    all_squares[0].forward(20) # the follow
    all_squares[0].left(90)


    # for squares in all_squares:
    #     squares.forward(20) --> this works but i need to change how the move
        #screen.update() #--> it could be here

# Set the screen to listen
screen.listen()

# The method turtle.onkey(function, key) is use to control the turtle with the keyboard
# 1- I need to create the functions without passing arguments because I need to pass these function in .onkey(fun,key)

#def move_forward():


# TODO: I need to tidy up my code a little be so all the parts that are related to the snake's behavior
#       and the snake'S appearance go into a separate class.
#       So that by the end of the whole project we should end up with three classes;
#       -a snake class   -a food class    - a Scoreboard  and all of these classes will be in separate files, managing only one thing.
#       The goal of the refactoring is so that  you could create separate files










screen.exitonclick()
