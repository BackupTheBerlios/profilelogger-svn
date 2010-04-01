from Finder import *

from Model.Project import *

class ProjectFinder(Finder):
    def __init__(self, parent):
        Finder.__init__(self, parent)
    def findAll(self):
        return self.doFindAll(Project, Project.name)
