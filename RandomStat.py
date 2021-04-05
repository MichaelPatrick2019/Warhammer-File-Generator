# Michael Patrick
# 4/5/21
# RandomStat

# Generates a random "statline", within good reason,
# for a valid Warhammer character
#
# Warhammer stats consist of 9 different numbers,
# in the following order...
# [Movement] [Weapon Skill] [Ballistic Skill] [Strength]
# [Toughness] [Wounds] [Attacks] [Leadership] [Armor Save]
#
# OR
#
# [M] [WS] [BS] [S] [T] [W] [A] [Ld] [Sv]
#
# Note the spaces in between each number.

import random


class RandomStat:
    rand = random


    # Generates a random movement movement number
    # Returns an integer
    def generate_movement(self):
        return self.rand.randrange(4, 20)

    # Generates a random weapon skill number
    # Returns an integer
    def generate_weapon_skil(self):
        return self.rand.randrange(2, 6)

    # Generates a random ballistic skill number
    # Returns an integer
    def generate_ballistic_skill(self):
        return self.rand.randrange(2, 6)

    # Generates a random strength value
    # Returns an integer
    def generate_strength(self):
        return self.rand.randrange(2, 10)

    # Generates a random toughness value
    # Returns an integer
    def generate_toughness(self):
        return self.rand.randrange(2, 10)

    # Generates a random wound value
    # Returns an integer
    def generate_wounds(self):
        return self.rand.randrange(1, 20)

    # Generates a random attack value
    # Returns an integer
    def generate_attacks(self):
        return self.rand.randrange(1, 8)

    # Generates a random leadership valie
    # Returns an integer
    def generate_leadership(self):
        return self.rand.randrange(10, 20)

    # Generates a random armor save
    # Returns an integer
    def generate_armor_save(self):
        return self.rand.randrange(2, 6)

    # Generates a randomized list of stats
    # Returns a string
    def generate_stats(self):
        result = ""
        result = (str(self.generate_movement()) + " "
                  + str(self.generate_weapon_skil()) + " "
                  + str(self.generate_ballistic_skill()) + " "
                  + str(self.generate_strength()) + " "
                  + str(self.generate_toughness()) + " "
                  + str(self.generate_wounds()) + " "
                  + str(self.generate_attacks()) + " "
                  + str(self.generate_leadership()) + " "
                  + str(self.generate_armor_save()))

        return result
