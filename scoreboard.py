from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0,280)
        self.pencolor("white")
        self.hideturtle()
        self.Score_update(0)


    def Score_update(self, score):
        self.clear()
        self.write(f"Score = {score} ", False, align="center", font=("Arial", 15, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", False, align="center", font=("Arial", 15, "normal"))