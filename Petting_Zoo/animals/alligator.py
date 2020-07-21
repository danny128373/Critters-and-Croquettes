from animals import Animal
from datetime import date
from movements import Walking, Swimming


class Alligator(Animal, Swimming, Walking):
    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Walking.__init__(self)
        Swimming.__init__(self)

    def feed(self):
        return f'While singing "Bodies", {self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}.'
