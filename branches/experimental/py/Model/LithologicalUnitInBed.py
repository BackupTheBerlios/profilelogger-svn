from DatasetInBed import DatasetInBed

class LithologicalUnitInBed(DatasetInBed):
    def __init__(self, bed, id=None, lithologicalUnit=None, begin=0, end=100, 
                 name=None, description=None):
        super(LithologicalUnitInBed, self).__init__(bed, id, begin, end, name, description)
        self.lithologicalUnit = lithologicalUnit
        self.bed.registerLithologicalUnit(self)

    def __str__(self):
        return u'Lithological Unit %s from %i to %i Percent of bed' % (self.lithologicalUnit,
                                                                       self.begin,
                                                                       self.end)
