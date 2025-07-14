class CounterTen:
    def __init__(self, limit):
        self.num = 1
        self.limit = limit
    def __iter__(self):
        return self
    def __next__(self):
        if self.num <= self.limit:
            temp = self.num
            self.num += 1
            return temp
        else:
            raise StopIteration
a1 = CounterTen(10)
print(next(a1))
for i in a1:
    print(i)