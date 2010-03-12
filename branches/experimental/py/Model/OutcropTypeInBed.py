from DatasetInBed import DatasetInBed

class OutcropTypeInBed(DatasetInBed):
    def __init__(self, bed, id=None, outcropType=None, begin=0, end=100, 
                 name=None, description=None):
        super(OutcropTypeInBed, self).__init__(bed, id, begin, end, name, description)
        self.outcropType = outcropType
        self.bed.registerOutcropType(self)

    def __str__(self):
        return u'Outcrop Type %s from %i to %i Percent of bed' % (self.outcropType,
                                                                 self.begin,
                                                                 self.end)
