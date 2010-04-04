from NamedDescribedDataset import NamedDescribedDataset

class ProfileColumn(NamedDescribedDataset):
    def __init__(self, id=None, name=None, description=None, headerClassName=None, bedPartClassName=None):
        NamedDescribedDataset.__init__(self, id, name, description)
        self.lithologicalUnits = list()
        self.headerClassName = headerClassName
        self.bedPartClassName = bedPartClassName
