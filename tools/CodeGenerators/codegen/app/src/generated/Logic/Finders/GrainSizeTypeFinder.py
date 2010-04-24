from InProjectFinderBase import *

from Model.GrainSizeType import *

class GrainSizeTypeFinder(InProjectFinderBase):
    def __init__(self, parent):
        InProjectFinderBase.__init__(self, parent)
    def findAll(self, project):
        if project is None:
            return None
        return self.doFindAllInProject(GrainSizeType, project)
