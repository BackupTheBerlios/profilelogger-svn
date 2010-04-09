from Finder import *

from Model.LengthUnit import *

class LengthUnitFinder(Finder):
    def __init__(self, parent):
        Finder.__init__(self, parent)
    def findAll(self):
        return self.doFindAll(LengthUnit, LengthUnit.name)
