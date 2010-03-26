from DatasetInBed import DatasetInBed

class FaciesInBed(DatasetInBed):
    def __init__(self, bed, id=None, facies=None, begin=0, end=100, 
                 name=None, description=None):
        super(FaciesInBed, self).__init__(bed, id, begin, end, name, description)
        self.facies = facies
        self.bed.registerFacies(self)

    def __str__(self):
        return u'Facies %s from %i to %i Percent of bed' % (self.facies,
                                                       self.begin,
                                                       self.end)
    def hasFacies(self):
        return self.facies is not None
