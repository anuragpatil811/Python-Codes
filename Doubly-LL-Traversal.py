class Node:
    def __init__(self, data):
        self.data = data
        self.nref = None
        self.pref = None
class doublyLL:
    def __init__(self):
        self.head = None
    def print_LL(self):
        if self.head is None:
            print("Linked List is empty !")
        else:
            n = self.head
            while n is not None:
                print(n.data, "--->", end = " ")
                n = n.nref
    def print_LL_reverse(self):
        if self.head is None:
            print("Linked List is empty !")
        else:
            n = self.head
            while n.nref is not None:
                print(n.data, "--->", end = " ")
                n = n.nref
            while n is not None:
                print(n.data, "--->", end = " ")
                n = n.pref
dL1 = doublyLL()
dL1.print_LL()  