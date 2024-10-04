class Person:
    def __init__(self, name, age, height, weight) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def eat(self):
        print('eat polao, mangsho')

    def excercise(self):
        raise NotImplementedError

class Cricketer(Person):
    def __init__(self, name, age, height, weight, team) -> None:
        self.team = team
        super().__init__(name, age, height, weight)
    
    def eat(self):
        print('eating veg')    #overRide

    def excercise(self):
        print('taka diye gham jhoray')

    def __add__(self, other):
        return self.age + other.age
    
    def __mul__(self, other):
        return self.height * other.height

    def __len__(self):
        return self.height

sakib = Cricketer('Sakib', 40, 68, 75, "BD")
mushi = Cricketer('mushi', 35, 60, 70, "BD")
# sakib.eat()
# sakib.excercise()
print(sakib + mushi)
print(sakib * mushi)
print(len(sakib))