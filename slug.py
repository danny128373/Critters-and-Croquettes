from animals import Animal


class Slug(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)
        self.slithers = True
