class A:
    def __init__(self, p1, p2):
        self.a1 = p1
        self.a2 = p2
        return print('this is the first parent class')
class B: 
    def __init__(self, p3):
        self.a3 = p3
        return print('this is second parent class')
class C(A, B):
    def __init__(self, p1, p2, p3, p4):
        self.a4 = p4 
        super().__init__(p1, p2)
        B.__init__(self, p3)
        return print(self.a1, self.a2, self.a3, self.a4)
c = C(100, 200, 300, 400)
