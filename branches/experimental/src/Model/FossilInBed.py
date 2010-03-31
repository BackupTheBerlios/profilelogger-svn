from DatasetInBed import DatasetInBed

class FossilInBed(DatasetInBed):
    def __init__(self, bed, id=None, fossil=None, begin=0, end=100, 
                 name=None, description=None):
        super(FossilInBed, self).__init__(bed, id, begin, end, name, description)
        self.fossil = fossil
        self.bed.registerFossil(self)

    def __str__(self):
        return u'Fossil %s from %i to %i Percent of bed' % (self.fossil,
                                                            self.begin,
                                                            self.end)
