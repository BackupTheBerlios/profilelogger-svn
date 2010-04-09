from DatasetInBed import DatasetInBed

class LithologyInBed(DatasetInBed):
    def __init__(self, bed, id=None, lithology=None, begin=0, end=100, 
                 name=None, description=None):
        super(LithologyInBed, self).__init__(bed, id, begin, end, name, description)
        self.lithology = lithology
    def hasLithology(self):
        return self.lithology is not None
    def __str__(self):
        return u'Lithology %s from %i to %i Percent of bed' % (self.lithology,
                                                       self.begin,
                                                       self.end)
