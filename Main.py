import turtle
import time


screen = turtle.Screen()
screen.title("Digital Clock")
screen.bgcolor("black")
screen.setup(width=1000, height=1000)
screen.tracer(0)


clock = turtle.Turtle()
clock.hideturtle()
clock.color("cyan")
clock.penup()


date_writer = turtle.Turtle()
date_writer.hideturtle()
date_writer.color("white")
date_writer.penup()


day_writer = turtle.Turtle()
day_writer.hideturtle()
day_writer.color("white")
day_writer.penup()


name = turtle.Turtle()
name.hideturtle()
name.color("magenta")
name.penup()


def update_clock():
    clock.clear()
    date_writer.clear()
    day_writer.clear()
    name.clear()

    current_time = time.strftime("%I:%M:%S %p")
    current_date = time.strftime("%d-%B-%Y")
    current_day = time.strftime("%A")

    clock.goto(0, 20)
    clock.write(
        current_time,
        align="center",
        font=("Times New Roman", 18, "bold")
    )

    date_writer.goto(170, -40)
    date_writer.write(
        current_date,
        align="center",
        font=("Times New Roman", 10, "bold")
    )

    day_writer.goto(-170, 150)
    day_writer.write(
        current_day,
        align="center",
        font=("Times New Roman", 20, "bold")
    )

    name.goto(400, -500)
    name.write(
        "SAM",
        align="center",
        font=("Times New Roman", 10, "bold")
    )

    screen.update()
    screen.ontimer(update_clock, 1000)


update_clock()
turtle.mainloop()