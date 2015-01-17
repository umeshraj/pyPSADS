# -*- coding: utf-8 -*-
"""
Created on Sat Jan 17 08:30:12 2015

@author: umesh
"""

from pythonds.basic import Queue


def hotPotato(nameList, num):
    """ simulating a game of hot potato """
    q = Queue()
    for name in nameList:  # make the queue of names
        q.enqueue(name)

    while q.size() > 1:
        print q.items
        for i in range(0, num):
            q.enqueue(q.dequeue())
        q.dequeue()
    return q.dequeue()

def main():
    print(hotPotato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7))

if __name__ == "__main__":
    main()
