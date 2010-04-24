from InProjectFinderBase import *

from Model.BeddingType import *

class BeddingTypeFinder(InProjectFinderBase):
    def __init__(self, parent):
        InProjectFinderBase.__init__(self, parent)
    def findAll(self, project):
        if project is None:
            return None
        return self.doFindAllInProject(BeddingType, project)
