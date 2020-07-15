from animals import Animal


class Horse(Animal):
    def __init__(self, name, species, movement):
        super().__init__(name, species)
        self.movement = movement
