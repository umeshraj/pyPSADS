# -*- coding: utf-8 -*-
"""
Created on Sun Jan 25 17:43:32 2015

@author: umesh
"""


class hashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def hashFunction(self, key):
        return key%self.size

    def rehash(self, oldHash):
        return (oldHash+1)%self.size

    def put(self, key, data):
        hashVal = self.hashFunction(key)

        if self.slots[hashVal] == None:  # slot is empty
            self.slots[hashVal] = key
            self.data[hashVal] = data
        else:  # the slot was full
            nextSlot = self.rehash(hashVal)
            while self.slots[nextSlot]!=None and self.slots[nextSlot] != key:
                nextSlot = self.rehash(nextSlot)

            if self.slots[nextSlot] == None: # slot is empty
                self.slots[nextSlot] = key
                self.data[nextSlot] = data
            else: # have to rewrite the data
                self.data[nextSlot] = data

    def get(self, key):
        hashVal = self.hashFunction(key)
        stop = False
        nextSlot = hashVal
        while self.slots[nextSlot] != key and not stop:
            nextSlot = self.rehash(nextSlot)
            if nextSlot == hashVal:  # back to start
                stop = True

        if stop:  # could not find the key
            return None
        else:  # found the key
            return self.data[nextSlot]

    def __getitem__(self, key):
        """ overload getitem method"""
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

H = hashTable()
H[54] = "cat"
H[26] = "dog"
H[93] = "lion"
H[17] = "tiger"
H[77] = "bird"
H[31] = "cow"
H[44] = "goat"
H[55] = "pig"
H[20] = "chicken"
H.slots
H.data
print(H[20])
print(H[17])
H[20] = 'duck'

print(H.data)
print(H[99])

