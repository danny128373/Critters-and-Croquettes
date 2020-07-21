from .attractions import Attraction


class PettingZoo(Attraction):

    def __init__(self, name, description):
        super().__init__(name, description)
        self.animals = list()

    def set_animals(self, animals):
        self.animals.extend(animals)

    def add_animal_pythonic(self, animal):
        try:
            if animal.walk_speed > -1:
                self.animals.append(animal)
        except AttributeError as ex:
            print(
                f'{animal} doesn\'t like to be petted, so please do not put it in the {self.name} attraction.')
