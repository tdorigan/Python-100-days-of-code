import turtle
from turtle import Turtle, Screen
import pandas


def write_country_name(country_name, xcor, ycor):
    writer.goto(float(xcor), float(ycor))
    writer.write(country_name)


data = pandas.read_csv("european-countries.csv")
screen = Screen()
screen.title("European Countries Quiz")
image = "europe_map.gif"
screen.addshape(image)
turtle.shape(image)

writer = Turtle()
writer.penup()
writer.hideturtle()

guessed_countries = []

game_over = False
while game_over is False:

    guess = screen.textinput(title=f"{len(guessed_countries)}/{len(data)} countries correct", prompt="Guess a country "
                                                                                                     "name:", )

    if guess is None:
        guess = ""
        game_over = True
    else:
        guess = guess.lower()

    if not data[data.country.str.lower() == guess].empty:
        if guess not in guessed_countries:
            guessed_countries.append(guess)
            country = data[data.country.str.lower() == guess]
            write_country_name(country.country.to_string(index=False),
                               country.x.to_string(index=False),
                               country.y.to_string(index=False))

    if len(guessed_countries) >= len(data):
        game_over = True

    if guess == "exit":
        game_over = True


writer.goto(0, 341)
writer.write(f"Final Score: {len(guessed_countries)}/{len(data)}", align="center", font=("Courier", 24, "normal"))

screen.mainloop()



