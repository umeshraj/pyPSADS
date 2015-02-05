# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 08:03:56 2015
URL: http://interactivepython.org/runestone/static/pythonds/Trees/SearchTreeImplementation.html
@author: umesh
"""

from TreeNode import TreeNode

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def put(self, key, val):
        """ main put function to put a new node in BST"""
        if self.root:  # tree is not empty
            self._put(key, val, self.root)
        else:
            newNode = TreeNode(key, val)
            self.root = newNode
        self.size += 1

    def _put(self, key, val, curNode):
        """ recursive call to find best node location """
        if key < curNode.key:  # put in left tree
            if curNode.hasLeftChild():  # left child is not empty
                self._put(key, val, curNode.leftChild)
            else:
                newNode = TreeNode(key, val, parent=self)
                curNode.leftChild = newNode
        else:  # key > curNode
            if curNode.hasRightChild():  # right child not empty
                self._put(key, val, curNode.rightChild)
            else:  # right child is empty
                newNode = TreeNode(key, val, parent=self)
                curNode.rightChild = newNode

    def __setitem__(self, key, val):
        """ overload the [] operator"""
        self.put(key, val)

    def get(self, key):
        """get the value of a node with given key"""
        if self.root is None:
            return None
        else:
            res = self._get(key, self.root)
            return res.val

    def _get(self, key, curNode):
        """ get the node with a given key"""
        if curNode is None:
            return None
        elif curNode.key == key:
            return curNode
        elif key > curNode.key:
            return self._get(key, curNode.rightChild)
        elif key < curNode.key:
            return self._get(key, curNode.leftChild)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        res = self.get(key)
        return res is not None

    def delete(self, key):
        """ delete a node with key """
        nodeToDelete = self._get(key, self.root)
        if nodeToDelete is None:  # key not in tree
            raise KeyError('Key not in tree')
        elif nodeToDelete is self.root:  # node is the root
            self.size -= 1
            self.root = None
        else:  # a node that is not a root has to be deleted
            self.removeNode(nodeToDelete)
            self.size -= 1

    def __delitem__(self, key):
        self.delete(key)

    def remove(self, node):
        """ delete a node """
        if node.isLeaf():  # easy case. Node is leaf
            if node.isLeftChild():  # node is left child
                node.parent.leftChild = None
            elif node.isRightChild():
                node.parent.rightChild = None

        elif node.hasBothChildren():  # has both children
            succNode = node.findSuccessor()  # find the successors
            succNode.spliceOut()
            node.key = succNode.key
            node.val = succNode.val

        else:  # node has only one child
            if node.hasLeftChild():
                if node.isLeftChild():
                    node.parent.leftChild = node.leftChild
                    node.leftChild.parent = node.parent
                elif node.isRightChild():
                    node.parent.rightChild = node.leftChild
                    node.leftChild.parent = node.parent
                else:  # node is root!
                    node.replaceNode(node.leftChild.key, node.leftChild.val,
                                     node.leftChild.leftChild,
                                     node.leftChild.rightChild)
            elif node.hasRightChild():
                if node.isLeftChild():
                    node.parent.leftChild = node.rightChild
                    node.rightChild.parent = node.parent
                elif node.isRightChild():
                    node.parent.rightChild = node.rightChild
                    node.rightChild.parent = node.parent
                else:  # node is root
                    node.replaceNode(node.rightChild.key, node.rightChild.val,
                                     node.rightChild.leftChild,
                                     node.rightChild.rightChild)

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

    def spliceOut(self):
        """ like delete except we give node instead of value"""
        if self.isleaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChildren():  # successor cannot have both children
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else:  # self has a right child
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.righChild.parent = self.parent

    def findMin(self):
        """ find the node with the smallest key """
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current


if __name__ == "__main__":
    mytree = BinarySearchTree()
    mytree[3] = "red"
    mytree[4] = "blue"
    mytree[6] = "yellow"
    mytree[2] = "at"

    print(mytree[6])
    print(mytree[2])