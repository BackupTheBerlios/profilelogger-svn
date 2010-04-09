from NamedDescribedDataset import NamedDescribedDataset

class LengthUnit(NamedDescribedDataset):
    microMetre = None
    def __init__(self, id=None, microMetre=None, name=None, description=None):
        super(LengthUnit, self).__init__(id, name, description)
        self.microMetre = microMetre
    def makeToolTip(self):
        return u'ID: %i\nName: %s\micrometre. %s\nDescription: %s' % (self.id, self.name, self.microMetre, self.description)
