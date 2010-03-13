from NamedDescribedDataset import NamedDescribedDataset

class GeologicalMeasurementType(NamedDescribedDataset):
    def __init__(self, id=None, name=None, description=None, isPlane=False):
        super(GeologicalMeasurementType, self).__init__(id, name, description)
        self.geologicalMeasurements = list()
        self.isPlane = isPlane
