from Finder import *

from Model.StratigraphicUnit import *

class StratigraphicUnitFinder(Finder):
    def __init__(self, parent):
        Finder.__init__(self, parent)
    def findAll(self, project):
        if project is None:
            return None
        return self.doFindAllInProject(StratigraphicUnit, StratigraphicUnit.name, project)
