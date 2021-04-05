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
def write_name():
    name_generator = RandomName()
    return name_generator.make_name()


# Generates a randomized stat line
# Returns a string
def make_stat():
    stat_maker = RandomStat()
    return stat_maker.generate_stats()

# Generates a random ranged weapon
# Returns a string
def make_ranged_weapon():
    ranged = RandomRangedWeapon()
    return ranged.make_weapon()


# Opens the given filename (which should be
# "somename.txt") and writes a series of
# characters to it
#
# filename is a string that gives the name of a file
def write_characters(file_name):
    with open(file_name, "w") as file:
        # Write name
        first_name = write_name()
        last_name = write_name()
        file.write(first_name + " " + last_name + "\n")

        # Write stats
        stats = make_stat()
        file.write(stats + "\n")

        # Psychic abilities (to do)
        file.write("None" + "\n")

        # Ranged Weapons
        ranged = make_ranged_weapon()
        file.write(ranged + "\n")

        file.close()


if __name__ == '__main__':
    filename = generate_file()
    write_characters(filename)
