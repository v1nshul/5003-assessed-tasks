
    
class Graph(object):
    
    def __init__(self, size):
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        print(self.adjMatrix)
        self.size = size

    #code written:
    def add_vertex(self):                                                                                                    
        self.adjMatrix.append([0 for i in range(self.size)])      #adding the vertex at the end 
                                                                  #of the matrix
    def add_edge(self,edge):
        self.adjMatrix[-1][-1] = edge                             #adding an edge by changing .
                                                                  #the last element
    def rem_edge(self,row,col,edge):
        self.adjMatrix[row][col] = edge                           #Change the edge at the 
                                                                  #specified position                                              
                                                                  #to the desired value.
    def printing(self):
        for row in self.adjMatrix:                                #printing the row one by one;
            print(*row)                                           #using the '*' to just print  
                                                                  #the elements.


   
def main():
        print("the graph is: ")                    #printing the graph
        g = Graph(5)
        g.printing()                              #using the function printing

        print("------Adding Vertex------------")   #adding a vertex
        g.add_vertex()
        g.printing()
        print("------Adding Edge---------")         #adding an edge
        g.add_edge(1)
        g.printing()
        print("---------Removing Edge---------")    #removing an edge
        g.rem_edge(1, 2, 3)
        g.printing()
if __name__ == '__main__':
      main()


