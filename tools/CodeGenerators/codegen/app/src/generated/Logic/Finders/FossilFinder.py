from InProjectFinderBase import *

from Model.Fossil import *

class FossilFinder(InProjectFinderBase):
    def __init__(self, parent):
        InProjectFinderBase.__init__(self, parent)
    def findAll(self, project):
        if project is None:
            return None
        return self.doFindAllInProject(Fossil, project)
