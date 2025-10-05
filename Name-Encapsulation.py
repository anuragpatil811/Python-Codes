class Hello:
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c
    def getvalues(self):
        print(self._a, self._b, self._c)
    def setvalues(self, value):
        self._c = value
a1 = Hello(2, 4, 6)
#a1.setvalues(10)
#a1.getvalues()
print(a1._a)
print(a1._b)
print(a1._c)
