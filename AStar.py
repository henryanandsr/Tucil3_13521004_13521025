import Node as n
import Graph as g
import Adjacent as a
import main as Main
import copy
import networkx as nx
import matplotlib.pyplot as plt

def inside(arr, el):
    #cek apakah adjacent el sudah ada di dalam arr
    # for i in range (len(arr)):
        # print(arr[i].start.name)
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
        # print("temp : ")
        # temp.display()
        # for i in range (len(temp.adjacent)):
            # print("adjacent : ")
            # temp.adjacent[i][0].display()
        # temp.adjacent.display()
        # expand ke node yang belum dikunjungi
        # temp.display()
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
                    # print('....................................................')
                    # tempGraph.display()
                    # print('heuristic' + str(heuristic))
                    # print('....................................................')
                    # print('--->  ' + str(tempGraph.cost))
            # print("masuk")
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
    # print(Adj1.x)
    # print(Adj2.x)
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
                    # print('....................................................')
                    # tempGraph.display()
                    # print('heuristic' + str(heuristic))
                    # print('....................................................')
                    # print('--->  ' + str(tempGraph.cost))
            # print("masuk")
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
        
# def main():
#     #baca dari test.txt
#     array_adj, array_node = Main.read("./test/Stuck.txt")
#     #minta input start dan end
#     for i in range (len(array_adj)):
#         print(str(i+1) + ". " + array_adj[i].start.name, end="")
#     idStart = int(input("Masukkan nomor node start : "))
#     idEnd = int(input("Masukkan nomor node end : "))
#     #jalankan AStar
#     result_Astar = AStar(array_adj, idStart-1, idEnd-1)
#     result_UCS = Main.UCS(array_node[idStart-1], array_node[idEnd-1], array_adj)
#     #print hasil
#     print("Hasil AStar : ")
#     #display graf hasil
#     if (result_Astar):
#         result_Astar.display()
#         print("Cost : " + str(result_Astar.purecost))



#         # Visualisasi graf
#         G = nx.DiGraph()
#         for tempAdj in array_adj:
#             for i in range(len(tempAdj.adjacent)):
#                 G.add_edge(tempAdj.start.name, tempAdj.adjacent[i][0].name, weight=tempAdj.adjacent[i][1])
#         # set warna edge
#         edge_colors = [G[u][v]['color'] if 'color' in G[u][v] else 'black' for u, v in G.edges()]
#         # set posisi node
#         pos = nx.spring_layout(G)
#         # gambar graf
#         nx.draw_networkx_edges(G, pos, edge_color=edge_colors, width=2, arrows=False)
#         nx.draw_networkx_nodes(G, pos, node_size=2000, node_color='lightblue')
#         nx.draw_networkx_labels(G, pos, font_size=7, font_family='sans-serif')
#         # set warna edge hasil
#         red_edges = [(result_Astar.list[i].start.name, result_Astar.list[i+1].start.name) for i in range(len(result_Astar.list)-1)]
#         nx.draw_networkx_edges(G, pos, edgelist=red_edges, edge_color='red', width=2, arrows=False)
#         nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'))
#         plt.show()
#     else:
#         print("Tidak ditemukan solusi")
# main()
