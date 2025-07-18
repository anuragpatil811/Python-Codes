class BST:
    def __init__(self, key):    #It is a special method in class and it is called when object is created. This method allows the class to initialize the attribute of class
        self.key = key
        self.lchild = None
        self.rchild = None
root = BST(10)
print(root.key)
#print(root.lchild)
root.lchild = BST(5)
print(root.lchild)
print(root.rchild)