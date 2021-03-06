# Michael Patrick
# 4/4/21
# Warhammer File Generator
#
# Creates a list of characters that fits the Warhammer
# Simulator format of file input, as shown below:
# [Character 1 Name]
# [Character 1 Stats]
# [Character Psychic Abilities]( if none, "None")
# Ranged[Character 1 Ranged]
# .
# .
# .
# Melee[Character 1 Melee 1]
# .
# .
# .
# [Space]
# [Character 2 Name]
# .
# .
# .
# etc.

from RandomName import RandomName
from RandomStat import RandomStat
from RandomRangedWeapon import RandomRangedWeapon
from RandomMeleeWeapon import RandomMeleeWeapon


# Generates a file, with the default name as
# "test.txt".
# filename is a string that will be appended with
# .txt... i.e. filename="newFile" will generate a
# file called "newFile.txt"
#
# newFileName is a string that represents the desired name of
# a file, that does NOT include ".txt"
#
# Returns a string that is the name of the file.
def generate_file(new_file_name="test"):
    file_name = new_file_name + ".txt"

    # any file of this name wil be erased!
    return file_name


# Generates a randomized name and returns
# it as a string
#
# Returns a string that is a random name
def write_name(last_name=False):
    name_generator = RandomName()
    return name_generator.create(last_name)


# Generates a randomized stat line
# Returns a string
def make_stat():
    stat_maker = RandomStat()
    return stat_maker.create()


# Generates a random ranged weapon
# Returns a string
def make_ranged_weapon():
    ranged = RandomRangedWeapon()
    return ranged.create()


# Generates a random melee weapon
# Returns a string
def make_melee_weapon():
    melee = RandomMeleeWeapon()
    return melee.create()


# Opens the given filename (which should be
# "somename.txt") and writes a series of
# characters to it
#
# filename is a string that gives the name of a file
def write_characters(file_name, numChar):
    with open(file_name, "w") as file:
        for x in range(int(numChar)):
            # Write name
            have_last = True;
            first_last_name = write_name(have_last)
            file.write(first_last_name + "\n")

            # Write stats
            stats = make_stat()
            file.write(stats + "\n")

            # Psychic abilities (to do)
            file.write("None" + "\n")

            # Ranged Weapons
            ranged = make_ranged_weapon()
            file.write("Ranged " + ranged + "\n")

            # Melee Weapons
            melee = make_melee_weapon()
            file.write("Melee " + melee)  # don't have extra \n at end of file

            if x != int(numChar) - 1:
                file.write("\n" * 2) #Space in between each character, except last line

        file.close()


if __name__ == '__main__':
    name = input("Please enter a file name: ")
    numChar = input("Please enter the number of characters you would like: ")

    filename = generate_file(name)
    write_characters(filename, numChar)
