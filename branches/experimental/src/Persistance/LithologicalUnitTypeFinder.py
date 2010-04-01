from Finder import *

from Model.LithologicalUnitType import *

class LithologicalUnitTypeFinder(Finder):
    def __init__(self, parent):
        Finder.__init__(self, parent)
    def findAll(self):
        return self.doFindAll(LithologicalUnitType, LithologicalUnitType.name)
