'''adv_1''' #remove method for binary tree
import math

class Node:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, cur_node):
        if data < cur_node.data:
            if cur_node.left is None:
                cur_node.left = Node(data)
            else:
                self._insert(data, cur_node.left)
        elif data > cur_node.data:
            if cur_node.right is None:
                cur_node.right = Node(data)
            else:
                self._insert(data, cur_node.right)
        else:
            print("Value already present in tree")

    def display(self, cur_node):
        lines, _, _, _ = self._display(cur_node)
        for line in lines:
            print(line)


    def _display(self, cur_node):
        
        if cur_node.right is None and cur_node.left is None:
            line = '%s' % cur_node.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        if cur_node.right is None:
            lines, n, p, x = self._display(cur_node.left)
            s = '%s' % cur_node.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2
        
        if cur_node.left is None:
            lines, n, p, x = self._display(cur_node.right)
            s = '%s' % cur_node.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        left, n, p, x = self._display(cur_node.left)
        right, m, q, y = self._display(cur_node.right)
        s = '%s' % cur_node.data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


    def remove(self,target):                                   #remove method for binary tree
        root = self.root                                       #root is the root of the tree
        if root == None:                                       #if root is None, return False
            return False                                       
        elif root.data == target:                              #if root is target
            if root.left is None and root.right is None:       #check if no children
                root = None                                    #if yes set root to None
            elif root.left and root.left is None:              #check if left child only
                root = root.left                               #if yes set root to left child
            elif root.left is None and root.right:             #check if right child only
                root = root.right                              #if yes set root to right child
            elif root.left and root.right:                     #check if left and right children
                self.if_left_n_right(root)                     #if yes call if_left_n_right function
                                                               #if root not target; 
        parent = None                                          #set parent to None
        node = root                                            #set node to root

        while node and node.data != target:                    #while loop to find target
            parent = node                                      #set parent to node             
            if target < node.data:                             #if target is less than node.data
                node = node.left                               #set node to node.left           
            elif target > node.data:                           #if target is greater than node.data
                node = node.right                              #set node to node.right

        if node is None or node.data != target:                #case 1: target not found
            return False                                       #return False
        elif node.left is None and node.right is None:         #case 2: target has no children
            if target < parent.data:                           #if target is less than parent.data
                parent.left = None                             #set parent.left to None
            else:                                              #if target is greater than parent.data
                parent.right = None                            #set parent.right to None                 
            return True                                        #return True
        elif node.left and node.right is None:                 #case 3: target has left child only
            if target < parent.data:                           #if target is less than parent.data
                parent.left = node.left
            else:
                parent.right = node.left    
            return True
        else:                                                  
            self.if_left_n_right(node)
            return True                                  #call if_left_n_right function
    def if_left_n_right(self,node):                             
        delNodeParent = node                               #case 5: has left and right children
        delNode = node.right                               #set delNodeParent to node
                                                            #set delNode to node.right     
        while delNode.left:                                #while loop to find leftmost node
            delNodeParent = delNode                        #set parent to delNode
            delNode = delNode.left                         #set delNode to node at left   

        node.data = delNode.data                           #store node.data to delNode

        if delNode.right:                                  #if delNode.right is not None
            if delNodeParent.data > delNode.data:          #if parent is greater than leftmost node
                delNodeParent.left = delNode.right         #set parent left to delNode right
            else:
                delNodeParent.right = delNode.right        #set parent right to delNode right
        else:
            if delNode.data < delNodeParent.data:          #if delNode is less than parent
                delNodeParent.left = None                  #set parent left to None
            else:
                delNodeParent.right = None                 #set parent right to None


bst = BinaryTree()
bst.insert(4)
bst.insert(2)
bst.insert(6)
bst.insert(1)
bst.insert(3)
bst.insert(5)
bst.insert(7)
bst.display(bst.root)
bst.remove(2)
bst.display(bst.root)