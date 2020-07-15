from animals import Animal
from alligator import Alligator
from bee import Bee
from cow import Cow

alligator = Alligator("Alligator", "American Alligator", "walk", "07/11/2020")
bee = Bee("Bee", "Western Honey Bee", "fly")
cow = Cow("Cow", "Bos taurus", "walk")


print(f"The {alligator.name} is an {alligator.species}. He likes to {alligator.movement}. He was admitted on {alligator.date_added}")
print(f"The {bee.name} is a {bee.species}. He likes to {bee.movement}.")
print(f"The {cow.name} is a {cow.species}. He likes to {cow.movement}.")
