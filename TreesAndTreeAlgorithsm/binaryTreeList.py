# -*- coding: utf-8 -*-
"""
Created on Thu Jan 29 08:08:58 2015
URL: http://interactivepython.org/runestone/static/pythonds/Trees/ListofListsRepresentation.html
@author: umesh
"""


def BinaryTree(rootVal):
    """ implementing a binary tree using lists"""
    return [rootVal, [], []]


def insertLeft(root, newVal):
    """ insert into the left branch"""
    curBranch = root.pop(1)  # current left branch
    if len(curBranch) > 0:  # left is not empty
        root.insert(1, [newVal, curBranch, []])
    else:  # left is empty
        root.insert(1, [newVal, [], []])
    # return root


def insertRight(root, newVal):
    """ insert into right branch"""
    curBranch = root.pop(2)
    if len(curBranch) > 0:  # right is not empty
        root.insert(2, [newVal, [], curBranch])
    else:  # right is empty
        root.insert(2, [newVal, [], []])
    # return root


def getRootVal(tree):
    return tree[0]


def setRootVal(tree, val):
    tree[0] = val


def getLeftChild(tree):
    return tree[1]


def getRightChild(tree):
    return tree[2]


if __name__ == "__main__":
    r = BinaryTree(3)
    insertLeft(r,4)
    insertLeft(r,5)
    insertRight(r,6)
    insertRight(r,7)

    l = getLeftChild(r)
    print(l)
    setRootVal(l,9)
    print(r)
    insertLeft(l,11)
    print(r)
    print(getRightChild(getRightChild(r)))
