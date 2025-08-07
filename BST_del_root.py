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
    def delete(self, data, curr):
        if self.key is None:
            print("Tree is empty!")
            return 
        if data < self.key:
           if self.lchild:
               self.lchild = self.lchild.delete(data, curr)
           else:
               print("Given node is not present in the tree")
        elif data > self.key:
            if self.rchild:
                self.rchild = self.rchild.delete(data, curr)
            else:
                print("Given node is not present in the tree")
        else:
            if self.lchild is None:
                temp = self.rchild
                if data == curr:
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    temp = None
                    return
                self = None
                return temp
            if self.rchild is None:
                temp = self.lchild
                if data == curr:
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    temp = None
                    return
                self= None
                return temp
            node = self.rchild
            while node.lchild:
                node = node.lchild                
            self.key = node.key
            self.rchild = self.rchild.delete(node.key, curr)
        return self
def count(node):
    if node is None:
        return 0
    return 1+count(node.lchild) + count(node.rchild)
    
root = BST(10)
list1 = [1, 12]
for i in list1:
    root.insert(i) 
print("Preorder")
root.preorder()
print()
if count(root) > 1:
    root.delete(10, root.key)
else:
    print("Can't perform deletion operation")
print("After Deleting")
root.preorder()