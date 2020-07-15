from animals import Animal


class Whale(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)
        self.swimming = True