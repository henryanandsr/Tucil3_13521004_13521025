import Node as n
import Graph as g
import Adjacent as a
import reader as read
import copy
import networkx as nx
import matplotlib.pyplot as plt

def inside(arr, el):
    #cek apakah adjacent el sudah ada di dalam arr
    for i in range (len(arr)):
        if (arr[i].start.name == el.name):
            return True
    return False
def isContainsEndNode(arr, el):
    #arr is graph
    for i in range (len(arr.list)):
        if (arr.list[i] == el):
            return True
    return False

def AStar(arrAdj, idxStart, idxEnd):
    found = False
    visited = []
    pqueue = []
    result = []
    temp = arrAdj[idxStart]

    #make a graph with start node
    parent = g.Graph(temp)
    # visited.append(temp)
    pqueue.append(parent)
    #inisiasi endnode
    endNode = arrAdj[idxEnd]
    if (idxEnd==idxStart):
        return parent
    idx = 0
    while not found:
        # print('---------------------------------------')
        #hapus dulu parentnya dari list
        del pqueue[idx]
        # ambil adjacent dari graf parent sampai dimana kita
        temp = parent.state
        for i in range (len(temp.adjacent)):
            tempParent = copy.deepcopy(parent)
            if not inside(visited, temp.adjacent[i][0]):
                #cari graf yang ingin dimasukkan
                for j in range (len(arrAdj)):
                    if arrAdj[j].start.name == temp.adjacent[i][0].name:
                        tempAdj = arrAdj[j]
                        break
                if (not tempAdj == None):
                    # print('tempAdj : ' + str(tempAdj.start.name))
                    # tempAdj.display()
                    tempParent.addAdjNode(tempAdj)
                    tempGraph = tempParent
                    #update cost
                    heuristic = (len(arrAdj)-len(tempGraph.list))*2
                    # heuristic = 0
                    tempGraph.cost = tempGraph.purecost + temp.adjacent[i][1] + heuristic
                    tempGraph.purecost = tempGraph.purecost + temp.adjacent[i][1]
                    #masukkan dalam result apabila menemukan hasil
                    if (isContainsEndNode(tempGraph, endNode)):
                        result.append(tempGraph)
                    #masukkan dalam pqueue dan visited
                    pqueue.append(tempGraph)    
        # cari node yang belum dikunjungi dengan f(n) terkecil
        if (len(pqueue)==0):
            break
        visited.append(temp)
        min = copy.deepcopy(pqueue[0])
        for i in range (len(pqueue)):
            if (pqueue[i].cost < min.cost):
                min = pqueue[i]
                idx = i
        parent = min
        # parent.display()
        #cari apakah sudah tidak bisa lagi / pencarian selesai 
        if (len(result)>0):
            min = result[0]
            for i in range (len(result)):
                #cari nilai minimal di result
                if (result[i].cost < min.cost):
                    min = result[i]
            #cari nilai minimal di pqueue
            min2 = pqueue[0]
            for i in range (len(pqueue)):
                if (pqueue[i].cost < min2.cost):
                    min2 = pqueue[i]
            if (min.cost <= min2.cost):
                found = True
    if found:
        for i in range (len(result)):
            if (result[i].cost == min.cost):
                return result[i]
    else:
        return None
def distance(Adj1, Adj2):
    #menghitung jarak antar node
    return ((Adj1.start.X - Adj2.start.X)**2 + (Adj1.start.Y - Adj2.start.Y)**2)**0.5
def AStarBonus(arrAdj, idxStart, idxEnd):
    found = False
    visited = []
    pqueue = []
    result = []
    temp = arrAdj[idxStart]
    #make a graph with start node
    parent = g.Graph(temp)
    # visited.append(temp)
    pqueue.append(parent)
    #inisiasi endnode
    endNode = arrAdj[idxEnd]
    if (idxEnd==idxStart):
        return parent
    idx = 0
    while not found:
        #hapus dulu parentnya dari list
        del pqueue[idx]
        # ambil adjacent dari graf parent sampai dimana kita
        temp = parent.state

        for i in range (len(temp.adjacent)):
            tempParent = copy.deepcopy(parent)
            if not inside(visited, temp.adjacent[i][0]):
                #cari graf yang ingin dimasukkan
                for j in range (len(arrAdj)):
                    if arrAdj[j].start.name == temp.adjacent[i][0].name:
                        tempAdj = arrAdj[j]
                        break
                if (not tempAdj == None):
                    # print('tempAdj : ' + str(tempAdj.start.name))
                    # tempAdj.display()
                    previous = copy.deepcopy(tempParent.state)
                    tempParent.addAdjNode(tempAdj)
                    tempGraph = tempParent
                    #update cost
                    heuristic = distance(tempGraph.state, arrAdj[idxEnd])
                    # heuristic = 0
                    tempGraph.cost = tempGraph.purecost + distance(previous, tempGraph.state) + heuristic
                    tempGraph.purecost = tempGraph.purecost + distance(previous, tempGraph.state)
                    #masukkan dalam result apabila menemukan hasil
                    if (isContainsEndNode(tempGraph, endNode)):
                        result.append(tempGraph)
                    #masukkan dalam pqueue dan visited
                    pqueue.append(tempGraph)    
        # cari node yang belum dikunjungi dengan f(n) terkecil
        if (len(pqueue)==0):
            break
        visited.append(temp)
        min = copy.deepcopy(pqueue[0])
        for i in range (len(pqueue)):
            if (pqueue[i].cost < min.cost):
                min = pqueue[i]
                idx = i
        parent = min
        # parent.display()
        #cari apakah sudah tidak bisa lagi / pencarian selesai 
        if (len(result)>0):
            min = result[0]
            for i in range (len(result)):
                #cari nilai minimal di result
                if (result[i].cost < min.cost):
                    min = result[i]
            #cari nilai minimal di pqueue
            min2 = pqueue[0]
            for i in range (len(pqueue)):
                if (pqueue[i].cost < min2.cost):
                    min2 = pqueue[i]
            if (min.cost <= min2.cost):
                found = True
    for i in range (len(result)):
        if (result[i].cost == min.cost):
            return result[i]