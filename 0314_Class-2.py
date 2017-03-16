class Dog:
    def __init__(self, name):
        self.name = name
        self.tricks =[]
        self.__money = 2000

    def add_trick(self, trick):
        self.tricks.append(trick)

    def earn(self, income):
        self.__money += income
    
    def spend(self, spending):
        self.__money -= spending

    def show_deposit(self):
        return self.__money

d = Dog('Mike')
print(d.show_deposit())
d.earn(3000)
print(d.show_deposit())
d.spend(1000)
print(d.show_deposit())
 



