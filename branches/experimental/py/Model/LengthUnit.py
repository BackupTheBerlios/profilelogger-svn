from NamedDescribedDataset import NamedDescribedDataset

class LengthUnit(NamedDescribedDataset):
    milliMetre = None
    def __init__(self, id=None, milliMetre=None, name=None, description=None):
        super(LengthUnit, self).__init__(id, name, description)
        self.milliMetre = milliMetre
    def makeToolTip(self):
        return u'ID: %i\nName: %s\nmm. %s\nDescription: %s' % (self.id, self.name, self.milliMetre, self.description)
