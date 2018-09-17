from node import Node

class Tree:
    """ Tree Class which a user interfaces"""
    def __init__(self):
        """ Constructor"""
        self.root = None
    
    def insert(self, val):
        """ Insert element (val)"""
        if self.root:
            return self.root.insert(val)
        else:
            self.root = Node(val)
            return True
        
    def find(self, val):
        """ Returns true if element (val) is present in the tree. Returns false otherwise"""
        if self.root:
            return self.root.find(val)
        else:
            return False
    
    def preorder(self):
        """ Pre-order traversal of the tree"""
        print ('Preorder Traversal')
        self.root.preorder()
    
    def inorder(self):
        """ In-order traversal of the tree"""
        print ('Inorder Traversal')
        self.root.inorder()
        
    def postorder(self):
        """ Post-order traversal of the tree"""
        print ('Postorder Traversal')
        self.root.postorder()
    
    def delete(self, val):
        """ Deletes the specified element (val) from the BST"""
        if self.root:
            self.root.delete(val)
        else:
            return False

if __name__ == '__main__':
	
	bst = Tree()
	bst.insert(10)
	bst.insert(15)
	bst.insert(20)
	bst.insert(22)
	bst.insert(12)
	bst.insert(11)
	bst.insert(14)


	bst.preorder()  # Pre-order traversal of tree before deleting element

	bst.delete(15)  # Deleting element with two children

	bst.preorder()  # Pre-order traversal of tree after deleting element
