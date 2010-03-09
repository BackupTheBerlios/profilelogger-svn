from Dataset import Dataset

class DatasetInBed(Dataset):
    def __init__(self, bed, id=None, begin=None, end=None, description=None):
        super(DatasetInBed, self).__init__(id)
        self.bed = bed
        self.begin = begin
        self.end = end
        self.description = None

    def hasBed(self):
        return self.bed is not None
