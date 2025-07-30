#Deletion except root node with one child
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
    def preorder(self):
        print(self.key, end= " ")
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()    
    def delete(self, data):
        if self.key is None:
            print("Tree is empty!")
            return 
        if data < self.key:
           if self.lchild:
               self.lchild = self.lchild.delete(data)
           else:
               print("Given node is not present in the tree")
        elif data > self.key:
            if self.rchild:
                self.rchild = self.rchild.delete(data)
            else:
                print("Given node is not present in the tree")
        else:
            if self.lchild is None:
                temp = self.rchild
                self = None
                return temp
            if self.rchild is None:
                temp = self.lchild
                self= None
                return temp
            node = self.rchild
            while node.lchild:
                node = node.lchild                
            self.key = node.key
            self.rchild = self.rchild.delete(node.key)
        return self
root = BST(10)
list1 = [20, 4, 30, 4, 1, 5, 6]
for i in list1:
    root.insert(i)
root.preorder()
print()
print("After deleting:")
root.delete(4)
root.preorder()