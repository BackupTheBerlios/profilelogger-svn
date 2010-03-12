from NamedDescribedDataset import NamedDescribedDataset

class StratigraphicUnit(NamedDescribedDataset):
    def __init__(self, stratigraphicUnitType=None, id=None, name=None, description=None):
        super(StratigraphicUnit, self).__init__(id, name, description)
        self.stratigraphicUnitType = stratigraphicUnitType
