from DatasetInBed import DatasetInBed

class TectonicUnitInBed(DatasetInBed):
    def __init__(self, bed, id=None, tectonicUnit=None, begin=0, end=100, 
                 name=None, description=None):
        super(TectonicUnitInBed, self).__init__(bed, id, begin, end, name, description)
        self.tectonicUnit = tectonicUnit
        self.bed.registerTectonicUnit(self)

    def __str__(self):
        return u'Tectonic Unit %s from %i to %i Percent of bed' % (self.tectonicUnit,
                                                                   self.begin,
                                                                   self.end)
    def hasTectonicUnit(self):
        return self.tectonicUnit is not None
