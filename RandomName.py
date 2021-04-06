# Michael Patrick
# 4/4/21
# RandomName
#
# Creates a random first and last name
# with capitalized first letters and
# lowercase others.

import random
from CharacterAspect import CharacterAspect


class RandomName(CharacterAspect):
    uppercaseAlphabet = [
        "A", "B", "C", "D", "E", "F",
        "G", "H", "I", "J", "K", "L",
        "M", "N", "O", "P", "Q", "R",
        "S", "T", "U", "V", "W", "X",
        "Y", "Z"
    ]

    lowercaseAlphabet = [
        "a", "b", "c", "d", "e", "f",
        "g", "h", "i", "j", "k", "l",
        "m", "n", "o", "p", "q", "r",
        "s", "t", "u", "v", "w", "x"
        "y", "z"
    ]

    def create(self):
        result = ""
        rand = random

        result += self.uppercaseAlphabet[rand.randrange(25)]
        for x in range(rand.randrange(1, 10)):
            result += self.lowercaseAlphabet[rand.randrange(25)]

        return result
