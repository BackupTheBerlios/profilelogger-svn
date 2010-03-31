from NamedDataset import NamedDataset

class NamedDescribedDataset(NamedDataset):
    description = None
    def __init__(self, id=None, name=None, description=None):
        super(NamedDescribedDataset, self).__init__(id, name)
        self.description = description
    def makeToolTip(self):
        return u'ID: %i\nName: %s\nDescription: %s' % (self.id, self.name, self.description)
