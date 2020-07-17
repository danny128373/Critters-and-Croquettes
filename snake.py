from animals import Animal


class Snake(Animal):
    def __init__(self, name, species, food):
        super().__init__(name, species, food)
        self.slithers = True
