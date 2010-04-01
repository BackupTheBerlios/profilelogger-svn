from Finder import *

from Model.SedimentStructure import *

class SedimentStructureFinder(Finder):
    def __init__(self, parent):
        Finder.__init__(self, parent)
    def findAll(self, project):
        if project is None:
            return None
        return self.doFindAllInProject(SedimentStructure, SedimentStructure.name, project)
