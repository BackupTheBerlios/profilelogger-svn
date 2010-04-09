from Finder import *

from Model.GeologicalMeasurementType import *

class GeologicalMeasurementTypeFinder(Finder):
    def __init__(self, parent):
        Finder.__init__(self, parent)
    def findAll(self):
        return self.doFindAll(GeologicalMeasurementType, GeologicalMeasurementType.name)
