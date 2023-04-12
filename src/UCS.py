import math
import queue

def UCS(start, end, adjacents):
    pque = queue.PriorityQueue ()
    pque.put((0, start)) 
    node_cost = {}
    node_cost[start] = 0
    path = []
    while not pque.empty():
        current = pque.get()
        if current[1] == end:
            temp = current[1]
            while(temp != start):
                path.append(temp)
                temp = temp.previous
            path.append(start)
            path = path[::-1]
            return path, node_cost[end]
        
        for i in range(len(adjacents)):
            if adjacents[i].start.name == current[1].name:
                for j in range(len(adjacents[i].adjacent)):
                    next_node = adjacents[i].adjacent[j][0]
                    cost = adjacents[i].adjacent[j][1]
                    new_cost = node_cost[current[1]] + cost
                    if next_node not in node_cost or new_cost < node_cost[next_node]:
                        node_cost[next_node] = new_cost
                        priority = new_cost
                        next_node.setPrev(current[1])
                        pque.put((priority, next_node))
    
    return None




def UCS_B(start, end, adjacents):
    weight_matrix = []
    pque = queue.PriorityQueue ()
    pque.put((0, start)) 
    node_cost = {}
    node_cost[start] = 0
    path = []

    for i in range(len(adjacents)):
        weight = []
        for j in range(len(adjacents[i].adjacent)):
            # weight.append(float((abs(adjacents[i].start.X) - abs(adjacents[i].adjacent[j][0].X))**2 + (abs(abs(adjacents[i].start.Y) - abs(adjacents[i].adjacent[j][0].Y))**2) ** 0.5))
            weight.append(distance(adjacents[i].start.X, adjacents[i].start.Y, adjacents[i].adjacent[j][0].X, adjacents[i].adjacent[j][0].Y))
        weight_matrix.append(weight)

    while not pque.empty():
        current = pque.get()
        if current[1] == end:
            temp = current[1]
            while(temp != start):
                path.append(temp)
                temp = temp.previous
            path.append(start)
            path = path[::-1]
            return path, node_cost[end]
        
        for i in range(len(adjacents)):
            if adjacents[i].start.name == current[1].name:
                for j in range(len(adjacents[i].adjacent)):
                    next_node = adjacents[i].adjacent[j][0]
                    cost = weight_matrix[i][j]
                    new_cost = node_cost[current[1]] + cost
                    if next_node not in node_cost or new_cost < node_cost[next_node]:
                        node_cost[next_node] = new_cost
                        priority = new_cost
                        next_node.setPrev(current[1])
                        pque.put((priority, next_node))
    
    return None

def distance(lat1, lon1, lat2, lon2):
    # Rumus Haversine
    R = 6371  
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)
    dlon = lon2_rad - lon1_rad
    dlat = lat2_rad - lat1_rad
    a = math.sin(dlat/2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = R * c
    return distance


# def main ():
#     adjacents, nodes = read("./test/Test.txt")
#     path, distance = UCS_2(nodes[2], nodes[3], adjacents)
#     print(distance)
#     for i in path:
#         print(i.name)
#     adjacents, nodes = readWithCoor("./test/alunalun.txt")
#     path, distance = UCS_B(nodes[5], nodes[2], adjacents)
#     print(distance)
#     for i in path:
#         print(i.name)
    
# main()
    