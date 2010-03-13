from NamedDescribedDataset import NamedDescribedDataset

class GeologicalMeasurementType(NamedDescribedDataset):
    def __init__(self, id=None, name=None, description=None,
                 name1=None, value1=None,
                 name2=None, value2=None,
                 name3=None, value3=None):
        super(GeologicalMeasurementType, self).__init__(id, name, description)
        self.geologicalMeasurements = list()
