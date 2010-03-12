from NamedDescribedDataset import NamedDescribedDataset

class LithologicalUnit(NamedDescribedDataset):
    def __init__(self, lithologicalUnitType=None, id=None, name=None, description=None):
        super(LithologicalUnit, self).__init__(id, name, description)
        self.lithologicalUnitType = lithologicalUnitType
