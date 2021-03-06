# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 08:29:33 2015
URL: http://interactivepython.org/runestone/static/pythonds/Trees/ParseTree.html
@author: umesh
"""


from binaryTree import BinaryTree
from pythonds.basic.stack import Stack
import operator  #standard operators as functions

def buildParseTree(inString):
    tokList = inString.split()
    pTree = BinaryTree("")
    pStack = Stack()
    pStack.push(pTree)
    curTree = pTree
    
    for token in tokList:
        if token == "(":
            pStack.push(curTree)
            curTree.insertLeft(BinaryTree(""))
            curTree = curTree.getLeftChild()
            
        elif token in "+-*/":
            curTree.setRootVal(token)
            pStack.push(curTree)
            curTree.insertRight(BinaryTree(""))
            curTree = curTree.getRightChild()
            
        elif token == ")":
            curTree = pStack.pop()

        else: # hoping this is a number
            curTree.setRootVal(int(token))
            curTree = pStack.pop()
            
    return pTree
        

def evaluateParseTree(parseTree):
    operDict = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}
    
    leftChild = parseTree.getLeftChild()
    rightChild = parseTree.getRightChild()
    if leftChild and rightChild:
        fn = operDict[parseTree.getRootVal()]  # get the operator
        return fn(evaluateParseTree(parseTree.getLeftChild()), \
        evaluateParseTree(parseTree.getRightChild()))

    else:
        return parseTree.getRootVal()            
            
if __name__ == "__main__":
    pt = buildParseTree("( ( 10 + 5 ) * 3 )")     
    print evaluateParseTree(pt)

    pt = buildParseTree("( 3 + ( 4 * 5 ) )")     
    print evaluateParseTree(pt)



