from Finder import *

from Model.OutcropType import *

class OutcropTypeFinder(Finder):
    def __init__(self, parent):
        Finder.__init__(self, parent)
    def findAll(self, project):
        if project is None:
            return None
        return self.doFindAllInProject(OutcropType, OutcropType.name, project)
