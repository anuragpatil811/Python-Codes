class A:
    def feature1(self):
        print("I am feature 1")
    def feature2(self):
        print("I am feature 2")
class B:
    def feature3(self):
        print("I am feature 3")
    def feature4(self):
        print("I am feature 4")
#class C(B):
#    def feature5(self):
#        print("I am in feature 5")
class C(A, B):
    def feature5(self):
        print("I am in feature 5")
a1 = A()
a1.feature1()
#a1.feature2()
b1 = B()
b1.feature3()
b1.feature4()

#Multilevel Inheritance
c1 = C()
c1.feature2()