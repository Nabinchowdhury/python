from abc import ABC, abstractmethod
#abc = abstract base class
class Animal(ABC):
    @abstractmethod
    def eat(self):
        print('eating food')
    def move(self):
        pass

class Monkey(Animal):
    def __init__(self, name) -> None:
        self.category = 'Monkey'
        self.name = name
        super().__init__()
    def eat(self):
        print('hey nana! eating banana')
layka = Monkey('mon')
# print(layka.name)
layka.eat()