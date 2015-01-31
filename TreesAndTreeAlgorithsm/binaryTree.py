# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 08:06:01 2015
URL: http://interactivepython.org/runestone/static/pythonds/Trees/NodesandReferences.html
@author: umesh
"""


class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None
    
    def insertLeft(self, newNode):
        """ insert left tree"""
        newTree = BinaryTree(newNode)
        newTree.leftChild = self.leftChild
        self.leftChild = newTree
        
    def insertRight(self, newNode):
        """ insert right child """
        newTree = BinaryTree(newNode)
        newTree.rightChild = self.rightChild
        self.rightChild = newTree
        
    def getLeftChild(self):
        return self.leftChild
        
    def getRightChild(self):
        return self.rightChild
        
    def setRootVal(self, val):
        self.key = val
        
    def getRootVal(self):
        return self.key
        
if __name__ == "__main__":
    r = BinaryTree('a')
    print(r.getRootVal())
    print(r.getLeftChild())
    r.insertLeft('b')
    print(r.getLeftChild())
    print(r.getLeftChild().getRootVal())
    r.insertRight('c')
    print(r.getRightChild())
    print(r.getRightChild().getRootVal())
    r.getRightChild().setRootVal('hello')
    print(r.getRightChild().getRootVal())

        
        