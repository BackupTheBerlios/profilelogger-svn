from NamedDescribedDataset import NamedDescribedDataset

class GrainSize(NamedDescribedDataset):
    def __init__(self, grainSizeType=None, id=None, name=None, description=None,
                 minSize=None, minSizeLengthUnit=None,
                 maxSize=None, maxSizeLengthUnit=None,
                 percentFromMinimum=0,
                 shortName=None):
        super(GrainSize, self).__init__(id, name, description)
        self.grainSizeType = grainSizeType
        self.minSize = minSize
        self.minSizeLengthUnit = minSizeLengthUnit
        self.maxSize = maxSize
        self.maxSizeLengthUnit = maxSizeLengthUnit
        self.percentFromMinimum = percentFromMinimum
        self.shortName = shortName
