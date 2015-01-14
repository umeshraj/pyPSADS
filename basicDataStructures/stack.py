# -*- coding: utf-8 -*-
"""
Created on Wed Jan 14 07:46:44 2015

@author: umesh
"""


class Stack:
    def __init__(self):
        self.items = []

    def push(self, newItem):
        self.items.append(newItem)

    def pop(self):
        return(self.items.pop())

    def peek(self):
        return(self.items[-1])

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)


s = Stack()
print(s.isEmpty())
s.push(4)
s.push('dog')
print(s.peek())
s.push(True)
print(s.size())
print(s.isEmpty())
s.push(8.4)
print(s.pop())
print(s.pop())
print(s.size())