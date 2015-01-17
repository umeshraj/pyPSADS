# -*- coding: utf-8 -*-
"""
Created on Fri Jan 16 08:32:34 2015

@author: umesh
"""

from pythonds.basic import Stack


def infixToPostfix(inFixStr):
    """ fn to convert infix to post fix"""
    postFixList = []
    s = Stack()
    chList = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    prec = {"(": 0, "+": 1, "-": 1, "*": 2, "/": 2}  # operator precedence

    tok = inFixStr.split(" ")
    for ch in tok:  # ch can be (,), operand, operator
        if ch in chList:  # the easy case when token is an operand
            postFixList.append(ch)
        elif ch == "(":  # easy case of (
            s.push(ch)
        elif ch == ")":  # keep popping and appending until (
            top = s.pop()
            while top != "(":
                postFixList.append(top)
                top = s.pop()  # pop next
        else:  # now we are at opeartors
            # pop higher order operators first
            while not s.isEmpty() and prec[s.peek()] > prec[ch]:
                postFixList.append(s.pop())
            s.push(ch)  # push current opeartor

    while not s.isEmpty():  # pop everything else in the stack
        postFixList.append(s.pop())
    return " ".join(postFixList)


print(infixToPostfix("A * B + C * D"))
print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))
print(infixToPostfix("( A + B ) * ( C + D )"))
print(infixToPostfix("( A + B ) * C"))
print(infixToPostfix("A + B * C"))