# -*- coding: utf-8 -*-
"""
Created on Sat Jan 17 08:04:10 2015

@author: umesh
"""


class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.insert(0, item)  # assuming 0 is rear of queue

    def dequeue(self):
        return self.items.pop()

    def __str__(self):
        outStr = [str(x) for x in self.items] #convert all items to string
        outStr = ", ".join(outStr)
        return "List vals: " + outStr


def main():
    q = Queue()
    q.enqueue(4)
    q.enqueue('dog')
    q.enqueue(True)
    print(q.size())
    print q

if __name__ == "__main__":
    main()