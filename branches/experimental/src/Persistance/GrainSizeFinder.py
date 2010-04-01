from Finder import *

from Model.GrainSize import *

class GrainSizeFinder(Finder):
    def __init__(self, parent):
        Finder.__init__(self, parent)
    def findAll(self):
        return self.doFindAll(GrainSize, GrainSize.name)
