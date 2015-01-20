# -*- coding: utf-8 -*-
"""
Created on Tue Jan 20 07:50:34 2015
URL: http://interactivepython.org/runestone/static/pythonds/Recursion/TowerofHanoi.html
@author: umesh
"""


def moveTower(ht, fromPole, toPole, withPole):
    """ base fn to move tower from beg to end using the use pole"""
    if ht >= 1:
        moveTower(ht-1, fromPole, withPole, toPole)
        moveDisc(fromPole, toPole)
        moveTower(ht-1, withPole, toPole, fromPole)

        
def moveDisc(fromPole, toPole):
    print "Moving from %s to %s" %(fromPole, toPole)

moveTower(3, "A", "B", "C")           
        