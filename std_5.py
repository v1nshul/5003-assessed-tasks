
class Node:
    def __init__(self, dataval = None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval
            
    def AtBeginning(self,newdata):
        NewNode = Node(newdata)

    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        last = self.headval
        while(last.nextval):
            last = last.nextval
        last.nextval = NewNode
    #insert method    
    def Insert(self,val_before,newdata):                    #defining insert method
        if val_before is None:                              #if val before is none                   
            print("No node to insert after")                #print no node to insert after      
            return
        else:
            new_node = Node(newdata)                        #else new node is new data  
            if self.headval is None:                        #if headval is empty             
                self.headval = new_node                     #headval is new node         
            else:
                current = self.headval                      #else current is headval
                while current.nextval is not val_before:    #check if we are at the previous node.
                    current = current.nextval               #If we are not at the node before the  
                                                            #target node,move to the next node.

                current.nextval = new_node                  #set the nextval of the node before the 
                                                            #node we want to insert after 
                                                            #to the new node

                new_node.nextval = val_before               #set the nextval of the new node
                                                            #to the node we want to insert after
                


list = SLinkedList()            
list.headval = Node("Mon") 
 
e2 = Node("Tue")
e3 = Node("Thur")    
e4 = Node("Fri")
e5 = Node("Sat")
list.headval.nextval = e2
e2.nextval = e3
e3.nextval = e4
e4.nextval = e5


list.AtEnd("Sun")
list.Insert(e3, "Wed")
list.listprint()


#the time complexity of the insert method is O(n) because it has to traverse the list to find the node before the node we want to insert after.
#the space complexity of the insert method is O(1) because it does not use any extra space.