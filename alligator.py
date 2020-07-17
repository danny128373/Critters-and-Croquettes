from animals import Animal
from datetime import date


class Alligator(Animal):
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food)
        self.swimming = True
        self.__chip_num = chip_num

    @property
    def chip_num(self):
        return self.__chip_num
        # try:
        #     return self.__chip_num
        # except AttributeError:
        #     return 0

    @chip_num.setter
    def chip_num(self, chip_num):
        pass
        # if type(chip_num) is int:
        #     self.__chip_num = chip_num
        # else:
        #     raise TypeError(
        #         "Please provide an integer value for the chip number.")

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
