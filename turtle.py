from animals import Animal


class Turtle(Animal):
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.__chip_num = chip_num
        self.swimming = True
