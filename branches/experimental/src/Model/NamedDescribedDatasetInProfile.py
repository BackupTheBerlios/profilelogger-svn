from NamedDescribedDataset import *

class NamedDescribedDatasetInProfile(NamedDescribedDataset):
    def __init__(self, id=None, profile=None, name=None, description=None, position=None):
        NamedDescribedDataset.__init__(self, id, name, description)
        self.profile = profile
        self.position = position
    def hasProfile(self):
        return self.profile is not None
    def hasPosition(self):
        return self.position is not None
