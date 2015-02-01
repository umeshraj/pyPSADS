# -*- coding: utf-8 -*-
"""
Created on Sat Jan 31 10:25:32 2015

@author: umesh
"""

from pythonds.trees.binaryTree import BinaryTree

def preOrder(tree):
    if tree:  # do this only if this is a tree
        print tree.getRootVal()
        preOrder(tree.getLeftChild())
        preOrder(tree.getRightChild())

def postOrder(tree):
    if tree:
        postOrder(tree.getLeftChild())
        postOrder(tree.getRightChild())
        print tree.getRootVal()

def inOrder(tree):
    if tree:
        inOrder(tree.getLeftChild())
        print tree.getRootVal()
        inOrder(tree.getRightChild())

if __name__ == "__main__":
    r = BinaryTree('Ch1')
    r.insertLeft('Sec1')
    r.insertRight('Sec2')
    r.getLeftChild().insertLeft("Sec 1.1")
    r.getLeftChild().insertRight("Sec 1.2")

    r.getRightChild().insertLeft("Sec 2.1")
    r.getRightChild().insertRight("Sec 2.2")

    print "Printing in pre order\n"
    preOrder(r)
    print "Printing in post order\n"
    postOrder(r)
    print "Printing in in-order"
    inOrder(r)