from DatasetInBed import DatasetInBed

class GeologicalMeasurementInBed(DatasetInBed):
    def __init__(self, bed, id=None, geologicalMeasurementType=None, begin=0, end=100, 
                 name=None, description=None, 
                 measurementType=None, strike=None, dip=None):
        super(GeologicalMeasurementInBed, self).__init__(bed, id, begin, end, name, description)
        self.bed.registerGeologicalMeasurement(self)
        self.geologicalMeasurementType = geologicalMeasurementType
        self.measurementType = measurementType
        self.strike = strike
        self.dip = dip
    def __str__(self):
        return u'Geological Measurement %s from %i to %i Percent of bed' % (self.geologicalMeasurementType,
                                                                            self.begin,
                                                                            self.end)
