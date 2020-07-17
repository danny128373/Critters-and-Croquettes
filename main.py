from animals import Animal
from alligator import Alligator
from cow import Cow
from deer import Deer
from fox import Fox
from giraffe import Giraffe
from horse import Horse
from snake import Snake
from worm import Worm
from slug import Slug
from salamander import Salamander
from hellbender import Hellbender
from turtle import Turtle
from fish import Fish
from shark import Shark
from whale import Whale
from pettingZoo import PettingZoo
from wetlands import Wetlands
from snakepit import Snakepit


# Creating an instance for every animal
alligator = Alligator("Allie", "alligator", "humans", 555444)
alligator.feed()
cow = Cow("Milkshake", "cow", "grass")
cow.feed()
deer = Deer("Bambi", "deer", "grapes")
fox = Fox("Sly Cooper", "fox", "bunnies")
giraffe = Giraffe("Jeffrey", "giraffe", "leaves")
horse = Horse("Al Capony", "horse", "hay")
snake = Snake("Danger Noodle", "snake", "mice")
worm = Worm("Slinky", "worm", "plants")
slug = Slug("Slug-E-Fresh", "slug", "plants")
salamander = Salamander("Natsu", "salamander", "dragonflies")
hellbender = Hellbender("Mud Devil", "hellbender", "crayfish")
turtle = Turtle("The Flash", "turtle", "snails")
fish = Fish("Phish Styx", "fish", "algae")
shark = Shark("Chum", "shark", "fish")
whale = Whale("Panda Whale", "whale", "seals")

# Creating areas for the animals
varmint_village = PettingZoo("Varmint Village")
varmint_village.set_animals([cow, deer, fox, giraffe, horse])

okavango = Wetlands("Okavango")
okavango.set_animals([alligator, turtle, fish, shark, whale])

village_hidden_in_the_mist = Snakepit("Village Hidden in the Mist")
village_hidden_in_the_mist.set_animals(
    [snake, worm, slug, salamander, hellbender])

# Printing animals in each area
for animal in varmint_village.animals:
    print(
        f'You can find {animal.name} the {animal.species} in {varmint_village.attraction_name}.')
for animal in okavango.animals:
    print(
        f'You can find {animal.name} the {animal.species} in {okavango.attraction_name}.')
for animal in village_hidden_in_the_mist.animals:
    print(
        f'You can find {animal.name} the {animal.species} in {village_hidden_in_the_mist.attraction_name}.')

# Making a private attribute in Alligator instance
print(alligator.chip_num)
alligator.chip_num = 550
print(alligator.chip_num)
