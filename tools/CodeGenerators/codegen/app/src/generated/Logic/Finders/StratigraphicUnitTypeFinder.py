from InProjectFinderBase import *

from Model.StratigraphicUnitType import *

class StratigraphicUnitTypeFinder(InProjectFinderBase):
    def __init__(self, parent):
        InProjectFinderBase.__init__(self, parent)
    def findAll(self, project):
        if project is None:
            return None
        return self.doFindAllInProject(StratigraphicUnitType, project)
