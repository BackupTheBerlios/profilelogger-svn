from Finder import *

from Model.Facies import *

class FaciesFinder(Finder):
    def __init__(self, parent):
        Finder.__init__(self, parent)
    def findAll(self, project):
        if project is None:
            return None
        return self.doFindAllInProject(Facies, Facies.name, project)
