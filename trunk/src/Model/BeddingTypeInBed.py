from DatasetInBed import DatasetInBed

class BeddingTypeInBed(DatasetInBed):
    def __init__(self, bed, id=None, beddingType=None, begin=0, end=100, 
                 name=None, description=None):
        super(BeddingTypeInBed, self).__init__(bed, id, begin, end, name, description)
        self.beddingType = beddingType
    def __str__(self):
        return u'Bedding Type %s from %i to %i Percent of bed' % (self.beddingType,
                                                                  self.begin,
                                                                  self.end)
    def hasBeddingType(self):
        return self.beddingType is not None
