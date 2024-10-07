class Person:
    def __init__(self, name, age, height, weight) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

class Cricketer(Person):
    cricketers = []
    def __init__(self, name, age, height, weight) -> None:
        super().__init__(name, age, height, weight)
        self.cricketers.append(self)
    
    def __gt__(self, other):
        return self.age > other.age

sakib = Cricketer('Sakib', 38, 68, 91)
musfiq = Cricketer('Rahim', 36, 68, 88)
kamal = Cricketer('Kamal', 39, 68, 94)
jack = Cricketer('Jack', 38, 68, 91)
kalam = Cricketer('Kalam', 37, 68, 95)
print(Cricketer.cricketers)
older_cricket = ''
for cricketer in Cricketer.cricketers:
    if not older_cricket:
        older_cricket = cricketer
    else:
        if(cricketer.__gt__(older_cricket)):
            older_cricket = cricketer

print(older_cricket.name)