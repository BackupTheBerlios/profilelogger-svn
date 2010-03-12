from NamedDescribedDataset import NamedDescribedDataset

class OutcropType(NamedDescribedDataset):
    def __init__(self, id=None, name=None, description=None):
        super(OutcropType, self).__init__(id, name, description)
