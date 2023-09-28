# Python program to create an undirected
# graph and add nodes and edges to a graph

# To import package
import pandas as pd
import networkx as nx
from matplotlib import pyplot as plt

# To create an empty undirected graph
G = nx.Graph()

# To add a node
#create 100 nodes
for i in range(100):
    G.add_node(i+1)



# To add an edge
# Note graph is undirected
# Hence order of nodes in edge doesn't matter
# attach each node to 5 distinct other nodes where degree of each node is 5
weight = 0
weights = 0
for i in range(50):
    for j in range(5):
        if i%10==4 and j==4:
            weight += 1
            G.add_edge(i+1, i+2, weight = weight)
            weight += 1
            G.add_edge(((i+50)//5)*5+j+1, ((i+50)//5)*5+j+2, weight = weight)
            continue
        if i%10==5 and j==0:
            continue
        else:
            weight += 1
            G.add_edge(i+1, ((i+50)//5)*5+j+1, weight = weight)
        if weight == 10:
            weight = 0
# #connect 45 to 5
# G.add_edge(45, 5)
            


G.add_edge(75, 95, weight=11)
G.add_edge(65, 55, weight=12)
G.add_edge(75, 65, weight=13)
G.add_edge(85, 55, weight=14)
G.add_edge(85, 95, weight=15)
G.add_edge(5, 15, weight=11)
G.add_edge(15, 25, weight=12)
G.add_edge(25, 35, weight=13)
G.add_edge(35, 45, weight=14)
G.add_edge(45, 5, weight=15)



# To get all the nodes of a graph
node_list = G.nodes()

# To get all the edges of a graph
edge_list = G.edges()
    

array1 = []
array2 = []
edge = list(edge_list)[0]

for edge in list(edge_list):
    array1.append(edge[0])
    array2.append(edge[1])
plt.rcParams["figure.figsize"] = [100, 100]
plt.rcParams["figure.autolayout"] = False
df = pd.DataFrame({'from': array1, 'to':array2})
#change colour of all nodes
routing_nodes = [35,85,25,75,65,15,5,55,95,45]
non_routing_nodes = []
for i in range(1, 101):
    if i not in routing_nodes:
        non_routing_nodes.append(i)
nx.draw_kamada_kawai(G, with_labels=True, node_color='r', nodelist=routing_nodes)
nx.draw_kamada_kawai(G, node_color='b', nodelist=non_routing_nodes)

#create dictionary with keys of as1 ,as2 having nodes connected to them
AS1 = []
AS2 = []
AS3 = []
AS4 = []
AS5 = []
for i in range(100):
    if 0<=i<=9 or 50<=i<=59:
        AS1.append(i+1)
    if 10<=i<=19 or 60<=i<=69:
        AS2.append(i+1)
    if 20<=i<=29 or 70<=i<=79:
        AS3.append(i+1)
    if 30<=i<=39 or 80<=i<=89:
        AS4.append(i+1)
    if 40<=i<=49 or 90<=i<=99:
        AS5.append(i+1)

def find_shortest_path(src, dest):
    #implementing hot potato for the source
    if (src in AS1 and dest in AS1) or (src in AS2 and dest in AS2) or (src in AS3 and dest in AS3) or (src in AS4 and dest in AS4) or (src in AS5 and dest in AS5): 
        shortest_path = nx.shortest_path(G, src, dest)
        total_distance = nx.path_weight(G, shortest_path, weight="weight")
    else:
        src_as_router_1 = 0
        src_as_router_2 = 0
        if src in AS1:
            src_as_router_1 = 5
            src_as_router_2 = 55
        if src in AS2:
            src_as_router_1 = 15
            src_as_router_2 = 65
        if src in AS3:
            src_as_router_1 = 25
            src_as_router_2 = 75
        if src in AS4:
            src_as_router_1 = 35
            src_as_router_2 = 85
        if src in AS5:
            src_as_router_1 = 45
            src_as_router_2 = 95

        src_router_1_path = nx.shortest_path(G, src, src_as_router_1)
        src_router_2_path = nx.shortest_path(G, src, src_as_router_2)
        src_distance_from_router_1 = nx.path_weight(G, src_router_1_path, weight="weight")
        src_distance_from_router_2 = nx.path_weight(G, src_router_2_path, weight="weight")

        min_distance_src_router = 0
        min_distance_src = 0
        min_distance_src_path = []

        if src_distance_from_router_1 < src_distance_from_router_2:
            min_distance_src_router = src_as_router_1
            min_distance_src = src_distance_from_router_1
            min_distance_src_path = src_router_1_path
        else:
            min_distance_src_router = src_as_router_2
            min_distance_src = src_distance_from_router_2
            min_distance_src_path = src_router_2_path

        dest_as_router_1 = 0
        dest_as_router_2 = 0

        if dest in AS1:
            dest_as_router_1 = 5
            dest_as_router_2 = 55
        if dest in AS2:
            dest_as_router_1 = 15
            dest_as_router_2 = 65
        if dest in AS3:
            dest_as_router_1 = 25
            dest_as_router_2 = 75
        if dest in AS4:
            dest_as_router_1 = 35
            dest_as_router_2 = 85
        if dest in AS5:
            dest_as_router_1 = 45
            dest_as_router_2 = 95

        dest_router_1_path = nx.shortest_path(G, dest_as_router_1, dest)
        dest_router_2_path = nx.shortest_path(G, dest_as_router_2, dest)
        dest_distance_from_router_1 = nx.path_weight(G, dest_router_1_path, weight="weight")
        dest_distance_from_router_2 = nx.path_weight(G, dest_router_2_path, weight="weight")

        min_distance_dest_router = 0
        min_distance_dest = 0
        min_distance_dest_path = []

        if dest_distance_from_router_1 < dest_distance_from_router_2:
            min_distance_dest_router = dest_as_router_1
            min_distance_dest = dest_distance_from_router_1
            min_distance_dest_path = dest_router_1_path
        else:
            min_distance_dest_router = dest_as_router_2
            min_distance_dest = dest_distance_from_router_2
            min_distance_dest_path = dest_router_2_path

        src_router_to_dest_router_path = nx.shortest_path(G, min_distance_src_router, min_distance_dest_router, weight="weight")
        src_router_to_dest_router = nx.path_weight(G, src_router_to_dest_router_path, weight="weight")

        total_distance = min_distance_src + src_router_to_dest_router + min_distance_dest

        shortest_path_with_dups = []
        shortest_path_with_dups.extend(min_distance_src_path)
        shortest_path_with_dups.extend(src_router_to_dest_router_path)
        shortest_path_with_dups.extend(min_distance_dest_path)

        shortest_path = []
        for i in shortest_path_with_dups:
            if i not in shortest_path:
                shortest_path.append(i)

    return [shortest_path, total_distance]


src = int(input("Enter The source node: "))
dest = int(input("Enter The Destination Node: "))
acquired_array = find_shortest_path(src, dest)
shortest_path = acquired_array[0]
shortest_distance = acquired_array[1]

# printing the shortest patha and the minimum distance

print("The Shortest Distance is "+str(shortest_distance))
print("The Shortest Path is from Node ", end="")

for i in range(len(shortest_path)):
    if i != len(shortest_path)-1:
        print(str(shortest_path[i]), end=" to ")
    else:
        print(str(shortest_path[i])+".")

nx.draw_kamada_kawai(G, node_color='g', nodelist=shortest_path)


#plottng the graph
plt.show()

#To delete all the nodes and edges
G.clear()