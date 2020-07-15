from animals import Animal
from datetime import date


class Giraffe(Animal):
    def __init__(self, name, species, food):
        super().__init__(name, species, food)
        self.walking = True
        self.shift = "morning"
