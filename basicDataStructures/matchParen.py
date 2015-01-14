# -*- coding: utf-8 -*-
"""
Created on Wed Jan 14 08:16:06 2015

@author: umesh
"""

from pythonds.basic import Stack

def parChecker(inList):
    """ function to match parenthesis """
    matched = True
    s = Stack()
    for ch in inList:
        if ch == "(":
            s.push(ch)
        else:  # ch is )
            if s.isEmpty():  # matching failed break
                matched = False
                break
            else:  # pop out matching ()
                s.pop()

    # matched should be true and there should be no more elements in stack
    return matched and s.isEmpty()


print(parChecker('((()))'))
print(parChecker('(()'))