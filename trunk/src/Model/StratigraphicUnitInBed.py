from DatasetInBed import DatasetInBed

class StratigraphicUnitInBed(DatasetInBed):
    def __init__(self, bed, id=None, stratigraphicUnit=None, begin=0, end=100, 
                 name=None, description=None):
        super(StratigraphicUnitInBed, self).__init__(bed, id, begin, end, name, description)
        self.stratigraphicUnit = stratigraphicUnit
    def __str__(self):
        return u'Stratigraphic Unit %s from %i to %i Percent of bed' % (self.stratigraphicUnit,
                                                                        self.begin,
                                                                        self.end)
    def hasStratigraphicUnit(self):
        return self.stratigraphicUnit is not None
