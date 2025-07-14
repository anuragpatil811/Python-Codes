class Hello:
    def __init__(self, a, b, c):
        self.a = a   # Public
        self._b = b  # Protected
        self.__c = c # Private
#Getter Method
    def getvalues(self):
        print(self.a, self._b, self.__c)
#Setter Method
    def setvalues(self, value):
        self.__c = value

# Create an instance of Hello
a1 = Hello(2, 4, 6)
a1.setvalues(10)
a1.getvalues()  # Corrected method name

# Accessing attributes directly
#print(a1.a)      # Public attribute, accessible directly
#print(a1._b)     # Protected attribute, accessible but should be avoided
#print(a1.__c)   # Private attribute, will raise an AttributeError
