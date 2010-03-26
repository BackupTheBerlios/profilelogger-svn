from Dataset import *

class GrainSizeTypeInProfile(Dataset):
    def __init__(self, id=None, grainSizeType=None, profile=None):
        super(Dataset, self).__init__(id)
        self.grainSizeType = grainSizeType
        self.profile = profile
    def hasGrainSizeType(self):
        return self.grainSizeType is not None
    def hasProfile(self):
        return self.profile is not None
