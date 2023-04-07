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
                adjacent.append([arrOfNode[node], numbers[node]])
        array_of_nodes.append(temp)
        array_of_adjacent.append(a.Adjacent(temp, adjacent))
        i += 1

    return array_of_adjacent, array_of_nodes
        
# a,b =(read("./test/Test.txt"))
# # print(a)
# for i in range (len(a)):
#     a[i].display()

# for i in range (len(b)):
#     b[i].display()