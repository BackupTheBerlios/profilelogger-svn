from Finder import *

from Model.LithologicalUnit import *

class LithologicalUnitFinder(Finder):
    def __init__(self, parent):
        Finder.__init__(self, parent)
    def findAll(self, project):
        if project is None:
            return None
        return self.doFindAllInProject(LithologicalUnit, LithologicalUnit.name, project)
