"""European Countries Quiz: Try to guess the names of the countries. When you guess correctly, the country's name
will appear on the map."""

import turtle
from turtle import Turtle, Screen
import pandas


def write_country_name(country_name, xcor, ycor):
    """Write the country's name on the map."""
    writer.goto(float(xcor), float(ycor))
    writer.write(country_name)


# reads a csv file that contains the coordinates of each country.
data = pandas.read_csv("european-countries.csv")

# setup screen
screen = Screen()
screen.title("European Countries Quiz")
image = "europe_map.gif"
screen.addshape(image)
turtle.shape(image)

# setup writer
writer = Turtle()
writer.penup()
writer.hideturtle()

guessed_countries = []

game_over = False
while game_over is False:

    # user input
    guess = screen.textinput(title=f"{len(guessed_countries)}/{len(data)} countries correct", prompt="Guess a country "
                                                                                                     "name:", )

    if guess is None:
        guess = ""
        game_over = True
    else:
        guess = guess.lower()

    # process user guess
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


# show final score
writer.goto(0, 341)
writer.write(f"Final Score: {len(guessed_countries)}/{len(data)}", align="center", font=("Courier", 24, "normal"))

screen.mainloop()



