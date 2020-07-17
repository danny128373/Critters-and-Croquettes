from animals import Animal


class Fish(Animal):
    def __init__(self, name, species, food):
        super().__init__(name, species, food)
        self.swimming = True
