from animals import Animal
from datetime import date
from movements import Walking


class Cow(Animal, Walking):
    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Walking.__init__(self)
        self.__chip_num = chip_num
        self.shift = "morning"

    def run(self):
        print(f"{self.name} the cow walks slowly as he/she moos.")

    def feed(self):
        return f'While singing "Last Resort", {self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}.'
