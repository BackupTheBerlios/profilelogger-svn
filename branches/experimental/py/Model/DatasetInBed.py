from NamedDescribedDataset import NamedDescribedDataset

class DatasetInBed(NamedDescribedDataset):
    def __init__(self, bed, id=None, begin=None, end=None, name=None, description=None):
        super(DatasetInBed, self).__init__(id, name, description)
        self.bed = bed
        self.begin = begin
        self.end = end
        self.description = None

    def hasBed(self):
        return self.bed is not None
