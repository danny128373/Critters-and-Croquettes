from .attractions import Attraction


class PettingZoo(Attraction):

    def __init__(self, name, description):
        super().__init__(name, description)
        self.animals = list()

    def set_animals(self, animals):
        self.animals.extend(animals)
