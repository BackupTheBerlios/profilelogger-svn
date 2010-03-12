from NamedDescribedDataset import NamedDescribedDataset

class StratigraphicUnitType(NamedDescribedDataset):
    def __init__(self, id=None, name=None, description=None):
        super(StratigraphicUnitType, self).__init__(id, name, description)
        self.stratigraphicUnits = list()
