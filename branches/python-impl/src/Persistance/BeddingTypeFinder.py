from Finder import *

from Model.BeddingType import *

class BeddingTypeFinder(Finder):
    def __init__(self, parent):
        Finder.__init__(self, parent)
    def findAll(self, project):
        if project is None:
            return None
        return self.doFindAllInProject(BeddingType, BeddingType.name, project)
