# This code will draw an image shaped like a cake.
# John Chaney

import turtle


# Function to draw a rectangle in Turtle
def rectangle(width, height):
    for i in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)


# Function to draw a triangle in Turtle
def triangle(size):
    for i in range(3):
        turtle.left(-120)
        turtle.back(size)


# Calling the triangle and rectangle functions with a cake function
def cake(width, height):
    for i in range(2):
        rectangle(width, height // 3)
        turtle.left(90)
        turtle.penup()
        turtle.forward(height // 3)
        turtle.pendown()
        turtle.right(90)
    rectangle(width, height // 3)
    turtle.penup()
    turtle.left(90)
    turtle.forward(3)
    turtle.right(90)
    turtle.forward(width // 2 - height // 2)
    turtle.pendown()
    triangle(height)


# Picking the color of the lines, turtle pensize, turtle speed and cake function arguments.
turtle.color("red")
turtle.pensize(2)
turtle.speed(2)
cake(250, 100)

# Code to move turtle to different areas and draw more cakes.
turtle.penup()
turtle.back(300)
turtle.pendown()
turtle.color("blue")
turtle.speed(2)
cake(100, 20)

turtle.penup()
turtle.right(90)
turtle.forward(150)
turtle.left(90)
turtle.pendown()
turtle.color("purple")
turtle.speed(2)
cake(150, 60)

turtle.Screen().exitonclick()
