# Michael Patrick
# 4/4/21
# RandomName
#
# Creates a random first and last name
# with capitalized first letters and
# lowercase others.

# CSV file generated from http://www.randat.com/

import random
from CharacterAspect import CharacterAspect
import csv


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

    firstNameDict = dict();
    lastNameDict = dict();
    numNames = 0;

    def __init__(self):
        with open('200RandomNamesRandatDotCom.csv', newline='') as csvfile:
            count = 1;
            reader = csv.reader(csvfile, delimiter = ',')
            for names in reader:
                self.firstNameDict[count] = names[0]
                self.lastNameDict[count] = names[1]
                count += 1
            self.numNames = count


    def create(self, include_last_name=False):
        result = ""
        rand = random

        result += self.firstNameDict[rand.randrange(self.numNames)]

        if include_last_name:
            result += " " + self.lastNameDict[rand.randrange(self.numNames)]

        return result

if __name__=='__main__':

    randoName = RandomName()
    print("Here are 20 random names:")
    for x in range(20):
        print(randoName.create())
