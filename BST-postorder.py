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
            else:
                self.rchild = BST(data)
    def search(self, data):
       if self.key == data:
           print("Node is found !")
           return 
       if data < self.key:
           if self.lchild:
               self.lchiild.search(data)
           else:
               print("Node is not present in tree!")
       else:
           if self.rchild:
               self.rchild.search(data)
           else:
               if self.rchild:
                   self.rchild.search(data)
               else:
                   print("Node is not present in tree !")
    def postorder(self):
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.key)
root = BST(10)
list1 = [6, 3, 1, 6, 98, 3, 7]
for i in list1:
    root.insert(i)
print("postorder")
root.postorder()