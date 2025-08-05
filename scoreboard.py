from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 15, "bold")
# Create the ScoreBoard Class
import os
import sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS  # used by PyInstaller
    except AttributeError:
        base_path = os.path.abspath(".")  # used in normal dev
    return os.path.join(base_path, relative_path)

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score= 0
        with open(resource_path("data.txt")) as data:         #To keep track of the score
            self.high_score = int(data.read())
        self.penup()
        self.goto(-30, 275)
        self.pencolor("white")
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    # reset the score board --> if the score the user obtained is higher than the high score It updates with the value of the current score

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(resource_path("data.txt"), mode="w") as data:
                data.write(str(self.score))
        self.score = 0
        self.update_scoreboard()


    # def game_over(self):
        #     self.goto(0,0)
        #     self.write(arg="GAME OVER ", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()













