'''
Author: excalibur-kvrv, modhtanmay 

Description: Implements the methods present in the Graph Interface using an adjacency matrix representation

Usage: create an object of the AdjacentMatrix class and call it's methods on the object.
       consider the graph as Shown below:  
      
      (0)******(1)*
       *         *  *
       *         *   (4)
       *         *  *
       (2)******(3)*

       INITIALIZATION:
       graph=AdjacentMatrix(num_vertices)
            EXAMPLES:
            graph.add_edge(0,1,2) #This adds an edge of weight 2 between vertices 0 and 1.
            graph.get_adjacent_vertices(0) #This returns a list of adjacent vertices to vertex 0.
            graph.get_edge_weight(0,1) #This returns the weight of the edge between 0 and 1.
            graph.get_indegree(0) #This returns the indegree of vertex 0.
            graph.get_outdegree(0) #This returns the outdegree of vertex 0. 
            graph.display() #This returns the set of edges of the graph with its weights.


'''
from graph_interface.graph import Graph


class AdjacentMatrix(Graph):
    def __init__(self, num_vertices, matrix=[], directed=False):
        super(AdjacentMatrix, self).__init__(num_vertices, directed)
        self._matrix = matrix
        if len(self._matrix) == 0:
            for _ in range(self.num_vertices):
                self._matrix.append([0]*self.num_vertices)
        self._visited = [0]*self.num_vertices
        self._visit_order = []

    def add_edge(self, v1, v2, weight=1):
        if v1 >= self.num_vertices or v2 >= self.num_vertices or v1 < 0 or v2 < 0:
            raise ValueError(f"Vertex v1: {v1} and v2: {v2} are out of bounds")
        self._matrix[v1][v2] = weight
        if self.directed == False:
            self._matrix[v2][v1] = weight

    def get_adjacent_vertices(self, v):
        if v >= self.num_vertices or v < 0:
            raise ValueError(f"Cannot access vertex {v}")
        adjacent_vertices = []
        for i in range(self.num_vertices):
            if self._matrix[v][i] > 0:
                adjacent_vertices.append(i)
        return adjacent_vertices

    def get_indegree(self, v):
        if v >= self.num_vertices or v < 0:
            raise ValueError(f"Cannot access vertex {v}")
        indegree = 0
        for i in range(self.num_vertices):
            if self._matrix[i][v] > 0:
                indegree += 1
        return indegree

    def get_outdegree(self, v):
        if v >= self.num_vertices or v < 0:
            raise ValueError(f"Cannot access vertes {v}")
        return len(self.get_adjacent_vertices(v))

    def get_edge_weight(self, v1, v2):
        if v1 >= self.num_vertices or v2 >= self.num_vertices or v1 < 0 or v2 < 0:
            raise ValueError(f"Vertex v1: {v1} and v2: {v2} are out of bounds")
        return self._matrix[v1][v2]
