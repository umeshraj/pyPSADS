# -*- coding: utf-8 -*-
"""
Created on Sat Jan 10 08:31:15 2015

Inheritance using Logic Gate example
URL: https://goo.gl/AEpgFw
@author: umesh
"""

class LogicGate:
    def __init__(self, gate_label):
        self.label = gate_label
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output


class BinaryGate(LogicGate):
    def __init__(self, gate_label):
        LogicGate.__init__(self, gate_label)

        self.pinA = None
        self.pinB = None

    def getPinA(self):
        return int(input("Enter Pin A input for gate "+ self.getLabel()+"-->"))

    def getPinB(self):
        return int(input("Enter Pin B input for gate "+ self.getLabel()+"-->"))

b = BinaryGate('ur')