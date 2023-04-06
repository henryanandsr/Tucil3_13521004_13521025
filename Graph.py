import Node as n

class Graph:
    def __init__(self, start, end, nodes):
        self.start = start
        self.end = end
        self.nodes = nodes
    
    def updateNodes(self, nodes):
        self.nodes.append(nodes)


