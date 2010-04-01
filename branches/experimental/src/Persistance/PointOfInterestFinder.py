from Finder import *

from Model.PointOfInterest import *

class PointOfInterestFinder(Finder):
    def __init__(self, parent):
        Finder.__init__(self, parent)
    def findAll(self, project):
        if project is None:
            return None
        return self.doFindAllInProject(PointOfInterest, PointOfInterest.name, project)
