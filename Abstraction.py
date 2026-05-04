from abc import ABC, abstractmethod 
class A(ABC):
    @abstractmethod
    def method1(self):
        pass
    def method2(self, param1, param2):
        self.attri1 = param1
        self.attri2 = param2
        return self.attri1, self.attri2
class B(A):
    def method1(self, param3, param4):
        self.attri3 = param3
        return self.attri3
q = B()
print(q.method1(100, 200))