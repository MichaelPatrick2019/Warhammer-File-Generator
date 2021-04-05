#Michael Patrick
#4/4/21
#Warhammer File Generator
#
#Creates a list of characters that fits the Warhammer
#Simulator format of file input, as shown below:
#[Character 1 Name]
#[Character 1 Stats]
#[Character Psychic Abilities]( if none, "None")
#Ranged[Character 1 Ranged]
#.
#.
#.
#Melee[Character 1 Melee 1]
#.
#.
#.
#[Space]
#[Character 2 Name]
#.
#.
#.
#etc.

from RandomName import RandomName

#Generates a file, with the default name as
#"test.txt".
#filename is a string that will be appended with
#.txt... i.e. filename="newFile" will generate a
#file called "newFile.txt"
#
#newFileName is a string that represents the desired name of
#a file, that does NOT include ".txt"
#
#Returns a string that is the name of the file.
def generateFile(newFileName="test"):
    filename = newFileName + ".txt"

    #any file of this name wil be erased!
    return filename

#Generates a randomized name and returns
#it as a string
#
#Returns a string that is a random name
def writeName():
    nameGenerator = RandomName()
    return nameGenerator.makeName()


#Opens the given filename (which should be
#"somename.txt") and writes a series of
#characters to it
#
#filename is a string that gives the name of a file
def writeCharacters(filename):
    with open(filename, "w") as file:
        firstName = writeName()
        lastName = writeName()
        file.write(firstName + " " + lastName + "\n")

        file.close()

if __name__ == '__main__':
    filename = generateFile()
    writeCharacters(filename)
