import Node as n
import Graph as g
import Adjacent as a
import main as Main
import copy

def inside(arr, el):
    #cek apakah adjacent el sudah ada di dalam arr
    print("Hai, ini inside")
    print('kita mau cek ' + str(el.name))
    print('di')
    for i in range (len(arr)):
        print(arr[i].start.name)
    for i in range (len(arr)):
        if (arr[i].start.name == el.name):
            return True
    print('salah')
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
    
    idx = 0
    while not found:
        print('---------------------------------------')
        #hapus dulu parentnya dari list
        del pqueue[idx]
        # ambil adjacent dari graf parent sampai dimana kita
        temp = parent.state
        print("temp : ")
        temp.display()
        for i in range (len(temp.adjacent)):
            print("adjacent : ")
            temp.adjacent[i][0].display()
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
                    print('tempAdj : ' + str(tempAdj.start.name))
                    tempAdj.display()
                    tempParent.addAdjNode(tempAdj)
                    tempGraph = tempParent
                    #update cost
                    heuristic = (len(arrAdj)-len(tempGraph.list))*2
                    # heuristic = 0
                    tempGraph.cost = tempGraph.cost + temp.adjacent[i][1] + heuristic
                    #masukkan dalam result apabila menemukan hasil
                    if (isContainsEndNode(tempGraph, endNode)):
                        p = len(tempGraph.list)-1
                        val = (len(arrAdj)-2)*2
                        while (p>0):
                            tempGraph.cost -= val
                            p-=1
                            val = val-2
                        result.append(tempGraph)
                    #masukkan dalam pqueue dan visited
                    pqueue.append(tempGraph)    
                    print('....................................................')
                    tempGraph.display()
                    print('heuristic' + str(heuristic))
                    print('....................................................')
                    print('--->  ' + str(tempGraph.cost))
            # print("masuk")
        # cari node yang belum dikunjungi dengan f(n) terkecil
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

def main():
    #baca dari test.txt
    array_adj, array_node = Main.read("./test/test.txt")
    #minta input start dan end
    for i in range (len(array_adj)):
        print(str(i+1) + ". " + array_adj[i].start.name, end="")
    idStart = int(input("Masukkan nomor node start : "))
    idEnd = int(input("Masukkan nomor node end : "))
    #jalankan AStar
    result = AStar(array_adj, idStart-1, idEnd-1)
    #print hasil
    print("Hasil AStar : ")
    #display graf hasil
    result.display()
    print("Cost : " + str(result.cost))
main()
