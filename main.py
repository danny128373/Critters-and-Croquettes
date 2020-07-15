from animals import Animal
from alligator import Alligator
from cow import Cow


alligator = Alligator("Allie", "alligator", "humans")
cow = Cow("Milkshake", "cow", "grass")
cow.feed()
alligator.feed()
print(cow)
print(alligator)
