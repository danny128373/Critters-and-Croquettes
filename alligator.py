from animals import Animal


class Alligator(Animal):
    def __init__(self, name, species, movement, date_added):
        super().__init__(name, species)
        self.movement = movement
        self.date_added = date_added
