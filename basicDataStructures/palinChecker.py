# -*- coding: utf-8 -*-
"""
Created on Sat Jan 17 18:20:06 2015

@author: umesh
"""

from pythonds.basic import Deque

def palchecker(inString):
    d = Deque()
    for ch in inString:
        d.addRear(ch)

    isPalin = True    
    while d.size() >=2 and isPalin:
        isPalin = d.removeFront() == d.removeRear()  # check if front = rear
    
    return isPalin
    
print(palchecker("lsdkjfskf"))
print(palchecker("radar"))
        