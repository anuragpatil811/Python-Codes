#a = 8
#b = 6
#print(type(a))
#print(type(b))
#print(a+b)
#print(int.__add__(a, b))
#print(int.__sub__(a, b))
#print(int.__add__(a, b))
class Students:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2
    def __add__(self, other):
        t1 = self.m1 + self.m2
        t2 = other.m1 + other.m2
        return t1 + t2
    def __gt__(self, other):
        t1 = self.m1 + self.m2
        t2 = other.m1 + other.m2
        if t1 > t2:
            return True
        else:
            return False
s1 = Students(50, 60)
s2 = Students(70, 60)
result = s1 + s2
print(result)
if s1 > s2:
    print("S1 Wins")
else:
    print("S2 Wins")