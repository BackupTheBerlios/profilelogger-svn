from Finder import *

from Model.TectonicUnitType import *

class TectonicUnitTypeFinder(Finder):
    def __init__(self, parent):
        Finder.__init__(self, parent)
    def findAll(self):
        return self.doFindAll(TectonicUnitType, TectonicUnitType.name)
