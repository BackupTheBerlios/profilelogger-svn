from DatasetInBed import DatasetInBed

class SedimentStructureInBed(DatasetInBed):
    def __init__(self, bed, id=None, sedimentStructure=None, begin=0, end=100, 
                 name=None, description=None):
        super(SedimentStructureInBed, self).__init__(bed, id, begin, end, name, description)
        self.sedimentStructure = sedimentStructure
    def __str__(self):
        return u'Sediment Structure %s from %i to %i Percent of bed' % (self.sedimentStructure,
                                                                        self.begin,
                                                                        self.end)
