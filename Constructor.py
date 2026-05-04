'''
class Car:
    def __init__(self, name, color, brand):
        self.name = name
        self.color = color
        self.brand = brand
        return print(self.name, self.color, self.brand)
car = Car("Seltos", "Black", "Kia")
'''
class Bank_App:
    def __init__(self, name, account_no, mpin):
        self.mpin = mpin
        self.name = name
        self.account_no = account_no
        self.balance = 1000
        return print(f'Welcome back dear customer {self.name}')
    def add_money(self, amount, mpin):
        self.mpin2 = mpin
        self.amount = amount
        if self.mpin2 == self.mpin:
            self.balance = self.balance + self.amount 
        else:
            print("Ask Anoushka for mpin")
virat = Bank_App("Virat Kohli", 18, 1234)
virat.add_money(1000000, 1234)
