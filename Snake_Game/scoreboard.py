from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        try:
            with open('scoreboard.txt', 'r') as f:
                self.high_score = int(f.read().strip())
                f.close()
        except FileNotFoundError:
            self.high_score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}, High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('scoreboard.txt', 'w') as f:
                f.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()
