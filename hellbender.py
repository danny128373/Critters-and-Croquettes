from animals import Animal


class Hellbender(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)
        self.slithers = True
