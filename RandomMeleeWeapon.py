# Michael Patrick
# 4/5/21
# RandomMeleeWeapon

# Generates a random melee weapon with the following
# format:
#
# Note: S = strength, AP = armor pierce, D = damage
#
# [Name] [S] [AP] [D] [Abilities]

import random
from RandomName import RandomName
from CharacterAspect import CharacterAspect


class RandomMeleeWeapon(CharacterAspect):
    rand = random

    # Generates a random name
    # Returns a string
    def generate_name(self):
        name = RandomName()
        return name.create()

    # Generates a random weapon strength
    # Returns a string
    def generate_weapon_strength(self):
        strength = self.rand.randrange(0, 10)
        if (strength == 0):
            return "User"
        else:
            return str(strength)

    # Generates a random armor pierce
    # Returns a int
    def generate_armor_pierce(self):
        return self.rand.randrange(0, 6)

    # Generates a random value for damage
    # Returns an int
    def generate_weapon_damage(self):
        return self.rand.randrange(1, 6)

    # Generates a random ability
    # Returns "None" for now..
    # Returns a string
    def generate_ability(self):
        return "None"

    # Generates a random melee weapon
    # Returns a string
    def create(self):
        return (self.generate_name() + " "
                + self.generate_weapon_strength() + " "
                + str(self.generate_armor_pierce()) + " "
                + str(self.generate_weapon_damage()) + " "
                + self.generate_ability())
