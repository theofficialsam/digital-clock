# Digital Clock 🕐

A simple digital clock built with Python using the built-in `Turtle` graphics module.

The clock displays the current time, date, day, and a name on a graphical window. The display automatically updates every second.

## Features

* Digital clock interface
* Displays current time
* Displays current date
* Displays current day
* Automatically updates every second
* Built with Python Turtle
* No external packages required

## Preview

The program opens a graphical window with a black background and displays:

```text
                 Tuesday

              11:25:42 PM

                       25-August-2026

                              SAM
```

The actual time and date are taken from the computer's system clock.

## How It Works

The program uses Python's built-in `time` module to retrieve the current time and date.

For example:

```python
time.strftime("%I:%M:%S %p")
```

returns the current time in 12-hour format.

The program uses Turtle's `ontimer()` function to call `update_clock()` every 1000 milliseconds:

```python
screen.ontimer(update_clock, 1000)
```

This creates the continuously updating clock.

## Technologies

* Python 3
* Turtle
* Time

Both `turtle` and `time` are included with Python, so no external dependencies are required.

## Requirements

Python 3.x

The program requires a Python installation with Turtle graphics support.

## Running the Program

Clone the repository:

```bash
git clone https://github.com/theofficialsam/digital-clock
```

Navigate into the project:

```bash
cd digital-clock
```

Run the program:

```bash
python Main.py
```

A graphical window will open displaying the clock.

## Concepts Practiced

* Python functions
* Turtle graphics
* Loops through scheduled callbacks
* System time and date
* String formatting
* GUI-style programming
* `ontimer()`
* Object creation
* Updating graphical elements

## Purpose

This project was created as a Python practice project to learn basic graphical programming and working with real-time system data.
