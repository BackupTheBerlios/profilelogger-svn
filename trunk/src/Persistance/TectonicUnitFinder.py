from Finder import *

from Model.TectonicUnit import *

class TectonicUnitFinder(Finder):
    def __init__(self, parent):
        Finder.__init__(self, parent)
    def findAll(self, project):
        if project is None:
            return None
        return self.doFindAllInProject(TectonicUnit, TectonicUnit.name, project)
