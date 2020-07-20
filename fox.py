from animals import Animal
from datetime import date


class Fox(Animal):
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.__chip_num = chip_num
        self.walking = True
        self.shift = "morning"

    def feed(self):
        return f'While singing "What Did the Fox Say?", {self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}'
