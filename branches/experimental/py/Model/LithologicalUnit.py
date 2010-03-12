from NamedDescribedDataset import NamedDescribedDataset

class LithologicalUnit(NamedDescribedDataset):
    def __init__(self, lithologicalUnitType=None, id=None, name=None, description=None,
                 minSize=None, minSizeLengthUnit=None,
                 maxSize=None, maxSizeLengthUnit=None,):
        super(LithologicalUnit, self).__init__(id, name, description)
        self.lithologicalUnitType = lithologicalUnitType
        self.minSize = minSize
        self.minSizeLengthUnit = minSizeLengthUnit
        self.maxSize = maxSize
        self.maxSizeLengthUnit = maxSizeLengthUnit
