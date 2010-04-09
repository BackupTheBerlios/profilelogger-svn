from NamedDescribedDataset import NamedDescribedDataset

class TectonicUnitType(NamedDescribedDataset):
    def __init__(self, id=None, name=None, description=None):
        super(TectonicUnitType, self).__init__(id, name, description)
        self.tectonicUnits = list()
