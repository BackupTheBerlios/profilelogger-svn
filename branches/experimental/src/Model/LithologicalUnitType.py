from NamedDescribedDataset import NamedDescribedDataset

class LithologicalUnitType(NamedDescribedDataset):
    def __init__(self, id=None, name=None, description=None):
        super(LithologicalUnitType, self).__init__(id, name, description)
        self.lithologicalUnits = list()
