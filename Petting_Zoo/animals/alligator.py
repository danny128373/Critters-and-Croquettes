from animals import Animal
from datetime import date


class Alligator(Animal):
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.swimming = True

    def feed(self):
        return f'While singing "Bodies", {self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}.'
