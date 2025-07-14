class Mobile:
    def __init__(self, brand, processor):
        self.brand = brand
        self.processor = processor
    def update(self):               #Updating the object
        self.processor = "Snapdragon 8gen 2"
    def compare(self, other):
        if self.processor == other.processor:
            return True
        else:
            return False   
m1 = Mobile("Oneplus", "A15")
m2 = Mobile("Apple", "A15")
#m1.update()
if m1.compare(m2):
    print("Processor are same")
else:
    print("Processor are not same")
print(m1.processor, m1.brand)
print(m2.processor, m2.brand)
