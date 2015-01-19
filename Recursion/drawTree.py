# -*- coding: utf-8 -*-
"""
Created on Mon Jan 19 12:42:14 2015

@author: umesh
"""

import turtle

def tree(branchLen, turt):
    if branchLen > 5:
        turt.forward(branchLen)
        turt.right(20)
        tree(branchLen - 15, turt)
        turt.left(40)
        tree(branchLen - 15, turt)
        turt.right(20)
        turt.backward(branchLen)
        
def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()

    t.left(90)  # face up
    t.up()  # take up tail before moving down
    t.backward(100)  # move down the screen
    t.down()  # put down the tail
    t.color("green")
    tree(100,t)
    myWin.exitonclick()
    
main()