# -*- coding: utf-8 -*-
"""
Created on Mon Jan 19 12:59:58 2015

@author: umesh

topic url: http://interactivepython.org/runestone/static/pythonds/Recursion/pythondsSierpinskiTriangle.html
"""

import turtle

def drawTriangle(triPoints, useColor, turt):
    """ function to draw a triangle given the 3 corners """
    p0 = triPoints[0]
    p1 = triPoints[1]
    p2 = triPoints[2]

    turt.up()  # don't draw
    turt.goto(p0[0],p0[1])  # reach the first point
        
    turt.down()  # get ready to color
    turt.fillcolor(useColor)  
    turt.begin_fill() # start coloring the inside of the triangle
    turt.goto(p1[0],p1[1])
    turt.goto(p2[0],p2[1])
    turt.goto(p0[0],p0[1])
    turt.end_fill()  # finished coloring the inside of the triangle


def getMidPoint(p1, p2):
    """function to get the mid points of two points p1, p2"""
    midX = (p1[0] + p2[0]) / 2.0
    midY = (p1[1] + p2[1]) / 2.0
    return([midX, midY])

def sierpinski(triPoints, order, turt):
    """ sierpinski triagle to draw 3 triangles """
    colormap = ['blue','red','green','white','yellow',
                'violet','orange']
    p0 = triPoints[0]
    p1 = triPoints[1]
    p2 = triPoints[2]
    drawTriangle(triPoints, colormap[order], turt)
    if order > 0:
        #compute mid points of various pairs
        p01 = getMidPoint(p0, p1)
        p12 = getMidPoint(p1, p2)
        p20 = getMidPoint(p2, p0)
        sierpinski([p0, p01, p20], order-1, turt)
        sierpinski([p1, p12, p01], order-1, turt)
        sierpinski([p2, p20, p12], order-1, turt)        


def main():
    myTurtle = turtle.Turtle()
    myWin    = turtle.Screen()
    myPoints = [[-100,-50],[0,100],[100,-50]]
    #drawTriangle(myPoints, myTurtle)
    sierpinski(myPoints, 3, myTurtle)
    myWin.exitonclick()

main()