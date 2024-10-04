class User:
    def __init__(self, name, age, money) -> None:
        self.name = name
        self.age = age
        self.money = money
    
    @property   #getter without setter is read-only
    def salary(self):
        return self.money

    @salary.setter 
    def salary(self, money):
        self.money += money

samsu = User('Kopa', 21, 10000)
samsu.salary = 200000000
print(samsu.salary)
