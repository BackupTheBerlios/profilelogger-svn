from Finder import *

from Model.ProfileColumn import *

class ProfileColumnFinder(Finder):
    def __init__(self, parent):
        Finder.__init__(self, parent)
    def findAll(self):
        return self.doFindAll(ProfileColumn, ProfileColumn.name)
