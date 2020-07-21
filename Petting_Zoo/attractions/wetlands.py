class Wetlands:

    def __init__(self, name):
        self.attraction_name = name
        self.description = "Danger! Alligators appear friendly, but they'll befriend you and stab you in the back"
        self.animals = list()

    def set_animals(self, animals):
        self.animals.extend(animals)
