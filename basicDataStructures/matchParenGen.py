# -*- coding: utf-8 -*-
"""
Created on Thu Jan 15 07:48:52 2015

@author: umesh
"""


from pythonds.basic import Stack


def parChecker(inString):
    """ Function to match three kinds of paranthesis"""
    openPar = '({['
    closePar = ')}]'
    balanced = True
    s = Stack()

    idx = 0
    while idx < len(inString) and balanced:
        ch = inString[idx]  # current character       

        if ch in openPar:  # in left par
            s.push(ch)
        else:  # ch not in left par
            if s.isEmpty():  # stack is empty
                balanced = False
            else:  # stack is not empty
                top = s.pop()
                balanced = isMatch(top, ch, openPar, closePar)
        idx += 1

    return balanced and s.isEmpty()


def isMatch(left, right, openPar, closePar):
    """ check if the left par is matched with the right"""
    leftIdx = openPar.index(left)
    rightIdx = closePar.index(right)
    return leftIdx == rightIdx


print(parChecker('{{([][])}()}'))
print(parChecker('[{()]'))
