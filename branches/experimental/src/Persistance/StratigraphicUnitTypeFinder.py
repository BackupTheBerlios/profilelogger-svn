from Finder import *

from Model.StratigraphicUnitType import *

class StratigraphicUnitTypeFinder(Finder):
    def __init__(self, parent):
        Finder.__init__(self, parent)
    def findAll(self):
        return self.doFindAll(StratigraphicUnitType, StratigraphicUnitType.name)
