class Snakepit:

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.animals = list()

    def set_animals(self, animals):
        self.animals.extend(animals)
