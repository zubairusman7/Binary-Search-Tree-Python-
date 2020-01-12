##  Binary Search Tree (BST) Python Implementation !!!

#  test comment 2

class Node:
    """ Node Class (which is hidden from the user)"""
    def __init__(self, val):
        """Constructor"""
        self.value = val
        self.left = None
        self.right = None
    
    def insert(self, val):
        """ Insert Function"""
        if self.value == val:
            return False
        elif val < self.value:
            if self.left:
                return self.left.insert(val)
            else:
                self.left = Node(val)
                return True
        else:
            if self.right:
                return self.right.insert(val)
            else:
                self.right = Node(val)
                return True
    
    def find(self, val):
        """ Returns true if the element is foudn in the tree. Returns false otherwise"""
        print('Entered find\n')
        if self.value == val:
            return True
        elif val > self.value:
            if self.right:
                return self.right.find(val)
            else:
                return False
        else:
            if self.left:
                return self.left.find(val)
            else:
                return False
    
    def preorder(self):
        """Pre-order traversal of the BST"""
        print(self.value)
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()
        return True

    def inorder(self):
        """In-order traversal of the BST"""
        if self.left:
            self.left.inorder()
        print(self.value)
        if self.right:
            self.right.inorder()
        return True
    
    def postorder(self):
        """Post-order traversal of the BST"""
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.value)
        return True
    
    def delete(self, val):
        """ Deletes the specified value (val) from the tree, and rearranges tree nodes appropriately """
        if self.value == val:
            if self.left and self.right:
                successor = self.right.find_successor()
                self.value = successor.value
                self.right = self.right.delete(self.value)
                return self
            elif self.left:
                print('Match found and only left node')
                l = self.left
                del self
                return l
            elif self.right:
                print('Match found and only right node')
                r = self.right
                del self
                return r
            else:
                print('Match found and no children')
                del self
                return None
            
        elif val > self.value:
            if self.right:
                self.right = self.right.delete(val)
                return self
            else:
                print('Node not found !!')
                return self
        else:
            if self.left:
                self.left = self.left.delete(val)
                return self
            else:
                print('Node not found !!')
                return self
    
    def find_successor(self):
        """ Finds the successor (next bigger element) of the current node """
        if self.left:
            return self.left.find_successor()
        else:
            return self
