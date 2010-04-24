from InProjectFinderBase import *

from Model.TectonicUnit import *

class TectonicUnitFinder(InProjectFinderBase):
    def __init__(self, parent):
        InProjectFinderBase.__init__(self, parent)
    def findAll(self, project):
        if project is None:
            return None
        return self.doFindAllInProject(TectonicUnit, project)
