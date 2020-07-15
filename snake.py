from animals import Animal


class Snake(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)
        self.slithers = True
