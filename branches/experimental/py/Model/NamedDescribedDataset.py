from NamedDataset import NamedDataset

class NamedDescribedDataset(NamedDataset):
    def __init__(self, id=None, name=None, description=None):
        super(NamedDescribedDataset, self).__init__(id, name)
        self.description = description
