from Finder import *

from Model.Profile import *

class ProfileFinder(Finder):
    def __init__(self, parent):
        Finder.__init__(self, parent)
    def findAll(self, project):
        if project is None:
            return None
        return self.doFindAllInProject(Profile, Profile.name, project)
