import math

class NodeB:
    def __init__(self,X, Y, name):
        self.X = X
        self.Y = Y
        self.name = name

class Node:

    def __init__(self, name, previous = None):
        self.name = name
        self.previous = previous

    def display(self):
        print(self.name)
    
    def setPrev(self, previous):
        self.previous = previous


    

    
    
    