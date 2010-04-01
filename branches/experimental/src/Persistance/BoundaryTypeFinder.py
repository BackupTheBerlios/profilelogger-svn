from Finder import *

from Model.BoundaryType import *

class BoundaryTypeFinder(Finder):
    def __init__(self, parent):
        Finder.__init__(self, parent)
    def findAll(self, project):
        if project is None:
            return None
        return self.doFindAllInProject(BoundaryType, BoundaryType.name, project)
