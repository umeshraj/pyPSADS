# -*- coding: utf-8 -*-
"""
Created on Sat Jan 10 08:31:15 2015

Inheritance using Logic Gate example
URL: https://goo.gl/AEpgFw
@author: umesh
"""

class LogicGate:
    def __init__(self, gate_label):
        self.label = gate_labe
        self.output = None

    def getLabel(self):
        return self.label()

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output