from Finder import *

from Model.GrainSizeType import *

class GrainSizeTypeFinder(Finder):
    def __init__(self, parent):
        Finder.__init__(self, parent)
    def findAll(self):
        return self.doFindAll(GrainSizeType, GrainSizeType.name)
