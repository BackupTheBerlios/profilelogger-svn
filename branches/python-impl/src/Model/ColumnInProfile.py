from Dataset import *

class ColumnInProfile(Dataset):
    def __init__(self, id=None, profile=None, profileColumn=None, position=None, width=None):
        Dataset.__init__(self, id)
        self.profile = profile
        self.profileColumn = profileColumn
        self.position = position
        self.width = width
    def hasProfile(self):
        return self.profile is not None
    def hasProfileColumn(self):
        return self.profileColumn is not None
    def hasPosition(self):
        return self.position is not None
    def hasWidth(self):
        return self.width is not None
