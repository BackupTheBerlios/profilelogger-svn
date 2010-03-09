from NamedDataset import NamedDataset

class LengthUnit(NamedDataset):
    def __init__(self, id=None, milliMetre=None, name=None):
        super(LengthUnit, self).__init__(id, name)
        self.milliMetre = milliMetre
