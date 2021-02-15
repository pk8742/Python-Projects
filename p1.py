# import turtle library
import turtle
import time

my_window = turtle.Screen()
my_window.bgcolor("blue")
# my_window.tracer(0)

# creates a graphics window
my_pen = turtle.Turtle()
my_pen.penup()
my_pen.goto(0,-50)
my_pen.pendown()
my_pen.circle(150)
my_pen.color("white")
"""
my_pen.forward(150)
my_pen.left(90)
my_pen.forward(75)
my_pen.color("white")
my_pen.pensize(12)
"""
turtle.done()  # to not destroy window immediately after program ends, we use turtle.done() method.
