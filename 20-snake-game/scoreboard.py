from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 12, 'bold')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0

        with open("data.txt") as data:
            self.high_score = int(data.read())

        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 280)
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score

            with open("data.txt", mode="w") as data:
                data.write(str(self.high_score))

        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)
