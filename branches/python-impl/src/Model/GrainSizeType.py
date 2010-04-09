from NamedDescribedDataset import NamedDescribedDataset

class GrainSizeType(NamedDescribedDataset):
    def __init__(self, id=None, name=None, description=None):
        super(GrainSizeType, self).__init__(id, name, description)
        self.grainSizes = list()
