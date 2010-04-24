from InProjectFinderBase import *

from Model.Lithology import *

class LithologyFinder(InProjectFinderBase):
    def __init__(self, parent):
        InProjectFinderBase.__init__(self, parent)
    def findAll(self, project):
        if project is None:
            return None
        return self.doFindAllInProject(Lithology, project)
