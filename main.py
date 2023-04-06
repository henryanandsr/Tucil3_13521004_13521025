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
    i = 0
    for line in lines:
        adjacent = []
        temp = n.Node(i)
        numbers = line.strip().split(' ')
        for node in range(len(numbers)):
            if numbers[node] != '0':
                adjacent.append([n.Node(int(node)), numbers[node]])

        array_of_nodes.append(temp)
        array_of_adjacent.append(a.Adjacent(temp, adjacent))
        i += 1
    
    return array_of_adjacent, array_of_nodes
        
