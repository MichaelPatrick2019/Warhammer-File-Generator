# Michael Patrick
# 4/5/21
# RandomRangedWeapon

from RandomName import RandomName
import random


# Generates a random ranged weapon in the following format:
# (S = strength, AP = Armor Pierce)
# [Name] [Range] [Type] [number of attacks] [S] [AP] [Abilities]
class RandomRangedWeapon:
    rand = random

    ranged_weapon_types = [
        "Heavy", "Assault", "Pistol",
        "Rapid-Fire", "Grenade"
    ]

    NUM_RANGE_TYPES = 5

    # Generates a random weapon name
    # Returns a string
    def generate_weapon_name(self):
        rand_name = RandomName()
        return rand_name.make_name()

    # Generates a random weapon range
    # Returns an int
    def generate_weapon_range(self):
        return self.rand.randrange(2, 40)

    # Generates a random weapon type
    # Returns a string
    def generate_weapon_type(self):
        return self.ranged_weapon_types[
            self.rand.randrange(0, self.NUM_RANGE_TYPES)]

    # Generate random number of attacks
    # Returns an int
    def generate_weapon_attacks(self):
        return self.rand.randrange(1, 20)

    # Generate random weapon strength
    # Returns an int
    def generate_weapon_strength(self):
        return self.rand.randrange(2, 10)

    # Generate random weapon armor piercing
    # Returns an int
    def generate_armor_pierce(self):
        return self.rand.randrange(0, 6)

    # Generate a random ability
    # Returns "None" for now.... (to do)
    # Returns a string
    def generate_ability(self):
        return "None"

    # Generates a completely random weapon
    # Returns a string
    def make_weapon(self):
        return (self.generate_weapon_name() + " "
                + str(self.generate_weapon_range()) + " "
                + self.generate_weapon_type() + " "
                + str(self.generate_weapon_attacks()) + " "
                + str(self.generate_weapon_strength()) + " "
                + str(self.generate_armor_pierce()) + " "
                + self.generate_ability() + " ")