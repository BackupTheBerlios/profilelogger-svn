from Finder import *

from Model.Color import *

class ColorFinder(Finder):
    def __init__(self, parent):
        Finder.__init__(self, parent)
    def findAll(self, project):
        if project is None:
            return None
        return self.doFindAllInProject(Color, Color.name, project)
