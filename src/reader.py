import Node as n
import Graph as g
import Adjacent as a

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

