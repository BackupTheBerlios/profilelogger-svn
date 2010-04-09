from Finder import *

from Model.Fossil import *

class FossilFinder(Finder):
    def __init__(self, parent):
        Finder.__init__(self, parent)
    def findAll(self, project):
        if project is None:
            return None
        return self.doFindAllInProject(Fossil, Fossil.name, project)
