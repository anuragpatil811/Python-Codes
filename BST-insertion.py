class BST:
    def __init__(self, key):
        self.key = key
        self.lchild = None
        self.rchild = None
    def insert(self, data):
        if self.key is None:
            self.key = data
            return 
        if self.key == data:
            return
        if self.key > data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
root = BST(10)
list1 = [20, 4, 30, 4, 1, 5, 6]
for i in list1:
    root.insert(i)