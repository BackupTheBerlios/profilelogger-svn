from Dataset import Dataset

class NamedDataset(Dataset):
    def __init__(self, id=None, name=None):
        super(NamedDataset, self).__init__(id)
        self.name = name
    def hasName(self):
        return self.name is not None
    def __str__(self):
        return u"<%s: ID: %i, Name: %s>" % (self.__class__.__name__, self.id, self.name)
