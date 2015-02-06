# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 08:22:50 2015

@author: umesh
"""

class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.val = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent
        self.balanceFactor = 0

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent.leftChild == self

    def isRightChild(self):
        return self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not self.leftChild and not self.rightChild

    def hasAnyChildren(self):
        return self.leftChild or self.rightChild

    def hasBothChildren(self):
        return self.leftChild and self.rightChild

    def replaceNodeData(self, key, val, lc, rc):
        self.key = key
        self.val = val
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

    def findSuccessor(self):
        if self.hasRightChild():
            succ = self.rightChild.findMin()
        else:  # no right child
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent
                else:
                    self.parent.rightChild = None  # remove self from search
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self  # replace it back!
        return succ

    def __iter__(self):
        if(self):
            if self.hasLeftChild():
                for elem in self.leftChild:
                    yield elem
            yield self.key
            if self.hasRightChild():
                for elem in self.rightChild:
                    yield elem
