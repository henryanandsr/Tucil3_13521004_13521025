import math

class NodeB:
    def __init__(self,name):
        self.name = name
    def setCoor(self,X,Y):
        self.X = X
        self.Y = Y
    def display(self):
        print(self.name)

class Node:

    def __init__(self, name, previous = None):
        self.name = name
        self.previous = previous

    def display(self):
        print(self.name)
    
    def setPrev(self, previous):
        self.previous = previous


    

    
    
    