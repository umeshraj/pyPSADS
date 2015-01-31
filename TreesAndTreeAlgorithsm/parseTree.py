# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 08:29:33 2015
URL: http://interactivepython.org/runestone/static/pythonds/Trees/ParseTree.html
@author: umesh
"""


from binaryTree import BinaryTree
from pythonds.basic.stack import Stack

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
        
        
if __name__ == "__main__":
    pt = buildParseTree("( ( 10 + 5 ) * 3 )")        




