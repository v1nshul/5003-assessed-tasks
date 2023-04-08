
from collections import defaultdict
import sys

class Graph():
    def __init__(self, size):
        self.edges = defaultdict(list)                              #dictionary of all connected nodes e.g. {'X': ['A', 'B', 'C', 'E'], ...}
        self.weights = {}                                           #dictionary of edges and weights e.g. {('X', 'A'): 7, ('X', 'B'): 2, ...}
        self.size = size
        self.dist = []
        for i in range(size):
            self.dist.append(sys.maxsize)
        self.previous = []
        for i in range(size):
            self.previous.append(None)
        
    
    def add_edge(self, from_node, to_node, weight):                 #bidirectional
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.weights[(from_node, to_node)] = weight
        self.weights[(to_node, from_node)] = weight


    def findSmallestNode(self): 
        smallest = self.dist[self.getIndex(self.Q[0])]
        result = self.getIndex(self.Q[0])
        for i in range(len(self.dist)):
            if self.dist[i] < smallest:
                node = self.unpoppedQ[i]
                if node in self.Q:
                    smallest = self.dist[i]
                    result = self.getIndex(node)
        return result
            

    def getIndex(self, neighbour):
        for i in range(len(self.unpoppedQ)):
            if neighbour == self.unpoppedQ[i]:
                return i


    def getPopPosition(self, uNode):
        result = 0
        for i in range(len(self.Q)):
            if self.Q[i] == uNode:
                return i
        return result


    def getUnvisitedNodes(self, uNode):
        resultList = []
        allNeighbours = self.edges[uNode]
        for neighbour in allNeighbours:
            if neighbour in self.Q:
                resultList.append(neighbour)
        return resultList          


    def dijsktra(self, start, end):                   #start and end are nodes              
        self.Q = []                                   #list of all nodes
        for key in self.edges:                        #add all nodes to list
            self.Q.append(key)                        
        for i in range(len(self.Q)):                 
            if self.Q[i] == start:                    #set distance of start node to 0
                self.dist[i] = 0                      #set previous of start node to None
        self.unpoppedQ = self.Q[0:]                   #list of all nodes that have not been popped from Q

        while self.Q:                                 #while Q is not empty                     
            u = self.findSmallestNode()               #find smallest node in Q                      
            if self.dist[u] == sys.maxsize:           #if smallest node is maxsize, then no path exists
                break                                           
            if self.unpoppedQ[u] == end:              #if smallest node is end node, then path found
                break

            uNode = self.unpoppedQ[u]                 #uNode is smallest node in Q                     

            #code here
            self.Q.pop(self.getPopPosition(uNode))                        #remove uNode from Queue        
            unvisitedNodes = self.getUnvisitedNodes(uNode)                #get all unvisited neighbours of uNode  
            for neighbour in unvisitedNodes:                              #for each neighbour of uNode
                alt = self.dist[u] + self.weights[(uNode, neighbour)]     #calculate new distance
                index = self.getIndex(neighbour)                          #get index of neighbour
                if alt < self.dist[index]:                                #if new distance is less than current distance
                    self.dist[index] = alt                                #update distance
                    self.previous[index] = uNode                          #update previous node
            
        shortest_path = []                      #list of shortest path                          
        shortest_path.insert(0, end)            #add end node to list
        u = self.getIndex(end)                  #get index of end node                                
        while self.previous[u] != None:         #while previous node is not None
            shortest_path.insert(0, self.previous[u])   #add previous node to list                        
            u = self.getIndex(self.previous[u])         #get index of previous node
        return shortest_path                            #return list of shortest path


graph = Graph(8)


edges = [
    ('O', 'A', 2),
    ('O', 'B', 5),
    ('O', 'C', 4),
    ('A', 'B', 2),
    ('A', 'D', 7),
    ('A', 'F', 12),
    ('B', 'C', 1),
    ('B', 'D', 4),
    ('B', 'E', 3),
    ('C', 'E', 4),
    ('D', 'E', 1),
    ('D', 'T', 5),
    ('E', 'T', 7),
    ('F', 'T', 3),
]
    

for edge in edges:
    graph.add_edge(*edge)


print(graph.dijsktra('O', 'T'))

