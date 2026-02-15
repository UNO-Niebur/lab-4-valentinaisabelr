#TurtleGraphics.py
#Name:Valentina Rodriguez
#Date: 2/15/2026
#Assignment: LAB 4

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)


def main():
    myTurtle = turtle.Turtle()
    # drawPolygon(myTurtle, 5) #draws a pentagon
    # drawPolygon(myTurtle, 8) #draws an octogon
def drawPolygon(myTurtle, sides, size):
    angle = 360 / sides
    for i in range(sides):
        myTurtle.forward(size)
        myTurtle.right(angle)
    # fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    # fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.
def fillCorner(myTurtle, corner, size):
    # draw the square first
    drawSquare(myTurtle, size)
    myTurtle.penup()
    myTurtle.backward(size)
    myTurtle.right(90)
    myTurtle.forward(size)
    myTurtle.left(90)
    myTurtle.pendown()
    myTurtle.begin_fill()
    if corner == 1:      # top right
        myTurtle.forward(size)
        myTurtle.left(90)
        myTurtle.forward(size)
        myTurtle.goto(myTurtle.xcor() - size, myTurtle.ycor() - size)
    elif corner == 2:    # top left
        myTurtle.left(90)
        myTurtle.forward(size)
        myTurtle.right(90)
        myTurtle.forward(size)
        myTurtle.goto(myTurtle.xcor() - size, myTurtle.ycor() - size)
    elif corner == 3:    # bottom left
        myTurtle.forward(size)
        myTurtle.left(90)
        myTurtle.forward(size)
        myTurtle.goto(myTurtle.xcor() - size, myTurtle.ycor() - size)
    elif corner == 4:    # bottom right
        myTurtle.forward(size)
        myTurtle.left(90)
        myTurtle.forward(size)
        myTurtle.goto(myTurtle.xcor() - size, myTurtle.ycor() - size)
    myTurtle.end_fill()
    # squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    # squaresInSquares(myTurtle, 3) #draws 3 concentric squares
def squaresInSquares(myTurtle, numSquares, startSize):
    size = startSize
    for i in range(numSquares):
        drawSquare(myTurtle, size)
        myTurtle.penup()
        myTurtle.backward(10)
        myTurtle.left(90)
        myTurtle.forward(10)
        myTurtle.right(90)
        myTurtle.pendown()
        size += 20

def main():
    myTurtle = turtle.Turtle()
    myTurtle.speed(0)

main()
