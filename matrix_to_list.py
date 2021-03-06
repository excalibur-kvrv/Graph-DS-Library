from representations.adjacent_set import AdjacentSet
from representations.adjacent_matrix import AdjacentMatrix
from matrix import matrix


graph=AdjacentMatrix(300,matrix,directed=False)

with open("set.txt","w") as file:
    file.write("vertex & (adjacent vertices,weight)\n")

for i in range(graph.num_vertices):
    with open("set.txt","a") as file:
        file.write(f"{i} ") 
        for v in graph.get_adjacent_vertices(i):
            file.write(f"{v} {graph.get_edge_weight(i,v)} ")
        file.write("\n")
                
with open("set.txt","r") as file:
    data=file.readlines()

graph_set=AdjacentSet(300,False)

set_list=data[1:]
for item in set_list:
    test_list=item[:len(item)-2]
    vertices_list=list(map(int,test_list.split()))
    for v in range(1,len(vertices_list)-1,2):
        graph_set.add_edge(vertices_list[0],vertices_list[v],vertices_list[v+1])

'''
# test data generation
with open("test.txt","w") as file:
    for i in range(graph.num_vertices):
        for j in graph.get_adjacent_vertices(i):
            file.write(f"{i}--->{j} weight {graph.get_edge_weight(i, j)}\n") 

with open("test1.txt","w") as file:
    for i in range(graph_set.num_vertices):
        for j in graph_set.get_adjacent_vertices(i):
            file.write(f"{i}--->{j} weight {graph_set.get_edge_weight(i, j)}\n") 
'''
print(graph_set.shortest_path_weighted(0,254))
    