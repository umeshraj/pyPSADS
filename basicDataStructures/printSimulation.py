# -*- coding: utf-8 -*-
"""
Created on Sat Jan 17 12:23:11 2015
URL: http://interactivepython.org/runestone/static/pythonds/BasicDS/SimulationPrintingTasks.html
@author: umesh
"""

from pythonds.basic import Queue
import random
# we need a printer and a task
class Printer:
    def __init__(self, ppm):
        self.ppm = ppm  # pages per minute
        self.currentTask = None  # a printer has a task
        self.timeRemaining = 0

    def tick(self):
        """ function to reduce the printer clock"""
        if self.currentTask is not None:
            self.timeRemaining -= 1
            if(self.timeRemaining <= 0):
                self.currentTask = None
                self.timeRemaining = 0  # just in case it goes negative

    def busy(self):
        return self.currentTask is not None

    def startNext(self, newTask):
        # assuming someone checks if printer is free
        self.currentTask = newTask
        self.timeRemaining = newTask.getPages() * 60/self.ppm  # in s

class Task:
    def __init__(self, currentTime):
        self.timeStamp = currentTime
        self.pages = random.randrange(1, 21)

    def getStamp(self):
        return self.timeStamp

    def getPages(self):
        return self.pages

    def waitTime(self, curTime):
        """ time the task has been waiting"""
        return curTime - self.timeStamp


def simulation(numSeconds, pagesPerMinute):
    """ make a simulation for numSeconds with printer
    that prints pagePerMinute"""
    labPrinter = Printer(pagesPerMinute)  # initialize printer
    printQueue = Queue()
    waitingTimes = []

    for currentSecond in range(numSeconds):
        # check if you should create a print task (1 every 180s)
        if newPrintTask():
            task = Task(currentSecond)
            printQueue.enqueue(task)

        # see if you can send it to the printer
        if (not labPrinter.busy()) and (not printQueue.isEmpty()):
            nextTask = printQueue.dequeue()
            waitingTimes.append(nextTask.waitTime(currentSecond))
            labPrinter.startNext(nextTask)

        labPrinter.tick() #reduce time on printer
    
    # print simulation results
    avgWaitTime = sum(waitingTimes)/len(waitingTimes)
    numRemain   = printQueue.size()
    print "Avg wait time %fs. There are %d items in queue" \
    %(avgWaitTime, numRemain)

def newPrintTask():
    """ see if random number is 180 """
    tmp = random.randrange(1, 181)
    return(tmp == 180)
    
# simulate the printing process for an hour with 5ppm printer
for i in range(10):
    simulation(3600, 5)    