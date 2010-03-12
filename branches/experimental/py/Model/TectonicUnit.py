from NamedDescribedDataset import NamedDescribedDataset

class TectonicUnit(NamedDescribedDataset):
    def __init__(self, tectonicUnitType=None, id=None, name=None, description=None):
        super(TectonicUnit, self).__init__(id, name, description)
        self.tectonicUnitType = tectonicUnitType
