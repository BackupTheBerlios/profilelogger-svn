from DatasetInBed import DatasetInBed

class GrainSizeInBed(DatasetInBed):
    def __init__(self, bed, id=None, grainSize=None, begin=0, end=100, 
                 name=None, description=None):
        super(GrainSizeInBed, self).__init__(bed, id, begin, end, name, description)
        self.grainSize = grainSize
        self.bed.registerGrainSize(self)

    def __str__(self):
        return u'Grain Size %s from %i to %i Percent of bed' % (self.grainSize,
                                                                self.begin,
                                                                self.end)
