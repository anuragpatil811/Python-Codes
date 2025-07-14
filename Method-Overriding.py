class Student:
    def sum(self, m1, m2):
        print(m1+m2)
class B(Student):
    #pass
    def sum(self, m1, m2):
        print((m1+m2)/10)
s1 = Student()
s1.sum(50, 40)