class A:
    def __init__(self):
        print("I am in class A ")
#class B(A):
class B:
    def __init__(self):
        super().__init__()
        print("I am in class B")
    def featureb(self):
        print("i am Feature B")
class C(B, A):
    pass
#a1 = A()
#b1 = B()
c1 = C()