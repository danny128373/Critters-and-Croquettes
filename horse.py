from animals import Animal
from datetime import date


class Horse(Animal):
    def __init__(self, name, species, food):
        super().__init__(name, species, food)
        self.walking = True
        self.shift = "morning"

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
