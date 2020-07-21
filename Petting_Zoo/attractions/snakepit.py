class Snakepit:

    def __init__(self, name):
        self.attraction_name = name
        self.description = "Danger! Some animals in here hug too hard"
        self.animals = list()

    def set_animals(self, animals):
        self.animals.extend(animals)
