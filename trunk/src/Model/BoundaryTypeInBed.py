from DatasetInBed import DatasetInBed

class BoundaryTypeInBed(DatasetInBed):
    def __init__(self, bed, id=None, boundaryType=None, begin=0, end=100, 
                 name=None, description=None):
        super(BoundaryTypeInBed, self).__init__(bed, id, begin, end, name, description)
        self.boundaryType = boundaryType
    def __str__(self):
        return u'Boundary Type %s from %i to %i Percent of bed' % (self.boundaryType,
                                                                   self.begin,
                                                                   self.end)
