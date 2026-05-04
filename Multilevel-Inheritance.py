class A:
    def __init__(self):
         pass 
    def method1(self):
         return 'this is from A class'
class B(A):
     def __init__(self):
          pass
     def method2(self):
          return super().method1() + ' this is from B class'
class C(B):
     def __init__(self):
          pass
     def method3(self):
          return super().method2() + ' this is from C class'
x = C()
print(x.method3())

