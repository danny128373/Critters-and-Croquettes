from animals import Animal
from datetime import date


class Cow(Animal):
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.__chip_num = chip_num
        self.walking = True
        self.shift = "morning"
