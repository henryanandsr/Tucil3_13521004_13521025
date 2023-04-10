import Node as n
import Graph as g
import Adjacent as a
import queue

def read(file):
    # Open the text file
    with open(file, 'r') as file:
    # Read the lines from the file
        lines = file.readlines()

    array_of_nodes = []
    array_of_adjacent = []
    arrOfNode = []
    i = 0
    # buat node
    for j in range (len(lines)):
        num = int(lines[0])
        if j > num :
            break
        if (j != 0):
            arrOfNode.append(n.Node(lines[j]))
    
    for j in range (num+1,len(lines)):
        adjacent = []
        temp = arrOfNode[i]
        numbers = lines[j].strip().split(' ')
        for node in range(len(numbers)):
            if numbers[node] != '0':
                adjacent.append([arrOfNode[node], int(numbers[node])])
        array_of_nodes.append(temp)
        array_of_adjacent.append(a.Adjacent(temp, adjacent))
        i += 1

    return array_of_adjacent, array_of_nodes

def readWithCoor(file):
    with open(file, 'r') as file:
    # Read the lines from the file
        lines = file.readlines()
    array_of_nodes = []
    array_of_adjacent = []
    i = 0
    prev = 0
    for j in range (len(lines)):
        num = int(lines[0])
        if j > num *2:
            break
        if (j != 0):
            if (j % 2 == 1):
                array_of_nodes.append(n.NodeB(lines[j]))
            else:
                temporaryCoor = lines[j].strip().split(' ')
                array_of_nodes[prev].setCoor(float(temporaryCoor[0]), float(temporaryCoor[1]))
                prev +=1
    for j in range(num*2+1,len(lines)):
        adjacent = []
        temp = array_of_nodes[i]
        numbers = lines[j].strip().split(' ')
        for node in range(len(numbers)):
            if numbers[node] != '0':
                adjacent.append([array_of_nodes[node]])
        array_of_adjacent.append(a.AdjacentB(temp, adjacent))
        i += 1
    return array_of_adjacent, array_of_nodes
        
def getNode(file):
    with open(file, 'r') as f:
        # Read the lines from the file
        lines = f.readlines()
    num = int(lines[0])
    if (len(lines) > num*2+1):
        a, b = readWithCoor(file)
        flag = True
    else:
        a, b = read(file)
        flag = False
    return b, flag
def UCS(start, end, adjacents):
    # pqueue = queue.PriorityQueue()
    pqueue = []
    visited = []
    # pqueue.put([0, start])
    pqueue.append([0, start])
    path = []

    while pqueue:
        min_val = min(pqueue) 
        min_idx = pqueue.index(min_val)  
        current = pqueue.pop(min_idx) 
        if current[1].name == end.name:
            visited.append(current[1].name)
            temp_node = current[1]
            while(temp_node != start):
                path.append(temp_node.name)
                temp_node = temp_node.previous
            path.append(start.name)
            path = path[::-1]
            # print(visited)
            return current[0], path
        
        if current[1].name not in visited:
            temp_node = current[1]
            visited.append(current[1].name)
            for i in range(len(adjacents)):
                if adjacents[i].start.name == current[1].name:
                    for j in range(len(adjacents[i].adjacent)):
                        if adjacents[i].adjacent[j][0].name not in visited:
                            adjacents[i].adjacent[j][0].setPrev(current[1])
                            # pqueue.put([int(current[0]) + adjacents[i].adjacent[j][1], adjacents[i].adjacent[j][0]])
                            pqueue.append([int(current[0]) + adjacents[i].adjacent[j][1], adjacents[i].adjacent[j][0]])
        else:   
            continue
            

    return None


def UCS_B(start, end, adjacents):

    # pqueue = queue.PriorityQueue()
    
    weight_matrix = []
    for i in range(len(adjacents)):
        weight = []
        for j in range(len(adjacents[i].adjacent)):
            weight.append(adjacents[i].start.getDistance(adjacents[i].adjacent[j][0]))

        weight_matrix.append(weight)

    pqueue = []
    visited = []
    # pqueue.put([0, start])
    pqueue.append([0, start])
    path = []

    while pqueue:
        min_val = min(pqueue) 
        min_idx = pqueue.index(min_val)  
        current = pqueue.pop(min_idx) 
        if current[1].name == end.name:
            visited.append(current[1].name)
            temp_node = current[1]
            while(temp_node != start):
                path.append(temp_node.name)
                temp_node = temp_node.previous
            path.append(start.name)
            path = path[::-1]
            print(visited)
            return current[0], path
        
        if current[1].name not in visited:
            temp_node = current[1]
            visited.append(current[1].name)
            for i in range(len(adjacents)):
                if adjacents[i].start.name == current[1].name:
                    for j in range(len(adjacents[i].adjacent)):
                        if adjacents[i].adjacent[j][0].name not in visited:
                            adjacents[i].adjacent[j][0].setPrev(current[1])
                            # pqueue.put([int(current[0]) + adjacents[i].adjacent[j][1], adjacents[i].adjacent[j][0]])
                            pqueue.append([int(current[0]) + weight_matrix[i][j], adjacents[i].adjacent[j][0]])
                            
        else:   
            continue
            

    return None


# def main ():
#     adjacents, nodes = read("./test/Test.txt")
#     # print(UCS(nodes[3], nodes[0], adjacents))
#     adjacents, nodes = readWithCoor("./test/buahbatu.txt")
#     # print(len(adjacents[0].adjacent))
#     print(UCS_B(nodes[3], nodes[6], adjacents))
#     # print("sate")
#     for el in adjacents:
#         el.display()
#     for el in nodes:
#         el.display()
# main()
    
