from NamedDescribedDataset import NamedDescribedDataset

class GrainSize(NamedDescribedDataset):
    def __init__(self, grainSizeType=None, id=None, name=None, description=None):
        super(GrainSize, self).__init__(id, name, description)
        self.grainSizeType = grainSizeType