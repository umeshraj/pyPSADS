# -*- coding: utf-8 -*-
"""
Created on Fri Jan 16 21:57:52 2015

@author: umesh
"""

from pythonds.basic import Stack

def postfixEval(postStr):
    s = Stack()
    tokList = postStr.split(" ")  # make a list for easy access

    for tok in tokList:
        if tok in "0123456789":
            s.push(int(tok))  # push operands to stack
        else:  # tok is an operator
            op2 = s.pop()
            op1 = s.pop()
            res = doMath(op1, op2, tok)
            s.push(res)  # push the result back onto the stack

    return s.pop()  # return the answer


def doMath(op1, op2, tok):
    if tok == "+":
        res = op1 + op2
    elif tok == "-":
        res = op1 - op2
    elif tok == "*":
        res = op1 * op2
    else:
        res = op1 / op2

    return res

print(postfixEval('7 8 + 3 2 + /'))
