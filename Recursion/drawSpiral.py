# -*- coding: utf-8 -*-
"""
Created on Mon Jan 19 08:32:44 2015

@author: umesh
"""

import turtle

myTurtle = turtle.Turtle()
myWin = turtle.Screen()


def drawSpiral(myTurtle, lineLen):
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        drawSpiral(myTurtle, lineLen-10)

drawSpiral(myTurtle, 100)
myWin.exitonclick()
