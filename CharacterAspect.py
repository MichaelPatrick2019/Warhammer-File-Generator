# Michael Patrick
# 4/5/21
# RandomMeleeWeapon

# Parent class of all random character
# aspect generators
from abc import abstractmethod


class CharacterAspect:

    # Everything MUST have a create() method
    @abstractmethod
    def create(self):
        pass

