from animals import Animal
from animals import Alligator
from animals import Cow
from animals import Deer
from animals import Fox
from animals import Giraffe
from animals import Horse
from animals import Snake
from animals import Worm
from animals import Slug
from animals import Salamander
from animals import Hellbender
from animals import Turtle
from animals import Fish
from animals import Shark
from animals import Whale
from attractions import PettingZoo
from attractions import Wetlands
from attractions import Snakepit
from movements import Walking, Slithering, Swimming


# Creating an instance for every animal
alligator = Alligator("Allie", "alligator", "humans", 1000)
alligator.feed()
cow = Cow("Milkshake", "cow", "grass", 1001)
cow.feed()
deer = Deer("Bambi", "deer", "grapes", 1002)
fox = Fox("Sly Cooper", "fox", "bunnies", 1003)
giraffe = Giraffe("Jeffrey", "giraffe", "leaves", 1004)
horse = Horse("Al Capony", "horse", "hay", 1005)
snake = Snake("Danger Noodle", "snake", "mice", 1006)
worm = Worm("Slinky", "worm", "plants", 1007)
slug = Slug("Slug-E-Fresh", "slug", "plants", 1008)
salamander = Salamander("Natsu", "salamander", "dragonflies", 1009)
hellbender = Hellbender("Mud Devil", "hellbender", "crayfish", 1010)
turtle = Turtle("The Flash", "turtle", "snails", 1011)
fish = Fish("Phish Styx", "fish", "algae", 1012)
shark = Shark("Chum", "shark", "fish", 1013)
whale = Whale("Panda Whale", "whale", "seals", 1014)

# Creating areas for the animals
varmint_village = PettingZoo(
    "Varmint Village", "Animals you can pet and walk with!")
varmint_village.set_animals([cow, deer, fox, giraffe, horse])

okavango = Wetlands(
    "Okavango", f"Careful with {alligator.name} and {shark.name}")
okavango.set_animals([alligator, turtle, fish, shark, whale])

village_hidden_in_the_mist = Snakepit(
    "Village Hidden in the Mist", "Danger! Some animals in here hug too hard")
village_hidden_in_the_mist.set_animals(
    [snake, worm, slug, salamander, hellbender])

# Printing animals in each area
for animal in varmint_village.animals:
    print(
        f'You can find {animal.name} the {animal.species} in {varmint_village.name}.')
for animal in okavango.animals:
    print(
        f'You can find {animal.name} the {animal.species} in {okavango.name}.')
for animal in village_hidden_in_the_mist.animals:
    print(
        f'You can find {animal.name} the {animal.species} in {village_hidden_in_the_mist.name}.')

# Making a private attribute in Alligator instance
print(alligator.chip_num)
alligator.chip_num = 500
print(alligator.chip_num)

# Overriding feed methods
print(alligator.feed())
print(cow.feed())
print(fox.feed())

# Multiple inheritance practice
alligator.swim()
alligator.run()
cow.run()

# Practicing duck typing
varmint_village.add_animal_pythonic(snake)
varmint_village.add_animal_pythonic(cow)
