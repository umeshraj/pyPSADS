# -*- coding: utf-8 -*-
"""
Created on Sat Jan 17 18:29:35 2015

@author: umesh
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return(self.data)

    def getNext(self):
        return self.next

    def setData(self, data):
        self.data = data

    def setNext(self, newNext):
        self.next = newNext


class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None
        
    def add(self, item):
        newNode = Node(item)
        newNode.setNext(self.head)
        self.head = newNode

    def size(self):
        linkSize = 0
        cur = self.head
        while cur is not None:
            linkSize += 1
            cur = cur.getNext()
        return linkSize
        
    def search(self, item):
        found = False
        cur = self.head
        while (cur is not None) and (not found):
            if cur.getData() == item:
                found = True
            cur = cur.getNext()
        return found
        
    def remove(self, item):
        """ assuming: item present"""
        prev = None
        cur = self.head
        found = False
        #find the item
        while (cur is not None) and (not found):
            if cur.getData() == item:
                found = True
            else:
                prev = cur
                cur = cur.getNext()
        
        #finished finding
        if prev == None:  # first element removal
            self.head = None
        else:
            prev.setNext(cur.getNext())
        

    def __str__(self):
        outStr = []
        cur = self.head
        while cur is not None:
            outStr.append(str(cur.getData()))
            cur = cur.getNext()
        return " ".join(outStr)
            
if __name__ == "__main__":
    ## testing
    myList = UnorderedList()
    myList.add(1)
    myList.add(10)
    print myList
    
    print(myList.search(-1))
    myList.remove(1)
    print(myList)