from Finder import *

from Model.ProfileAssembly import *

class ProfileAssemblyFinder(Finder):
    def __init__(self, parent):
        Finder.__init__(self, parent)
    def findAll(self, project):
        if project is None:
            return None
        return self.doFindAllInProject(ProfileAssembly, ProfileAssembly.name, project)
