from InProjectFinderBase import *

from Model.LithologicUnit import *

class LithologicUnitFinder(InProjectFinderBase):
    def __init__(self, parent):
        InProjectFinderBase.__init__(self, parent)
    def findAll(self, project):
        if project is None:
            return None
        return self.doFindAllInProject(LithologicUnit, project)
