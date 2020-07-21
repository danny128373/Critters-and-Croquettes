class Snakepit:

    def __init__(self, name, description):
        self.attraction_name = name
        self.description = description
        self.animals = list()

    def set_animals(self, animals):
        self.animals.extend(animals)
