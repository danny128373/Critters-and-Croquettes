from animals import Animal
from datetime import date


class Alligator(Animal):
    def __init__(self, name, species, food):
        super().__init__(name, species, food)
        self.swimming = True

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
