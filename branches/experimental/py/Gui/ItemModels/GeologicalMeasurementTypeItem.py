from StandardItem import StandardItem

class GeologicalMeasurementTypeItem(StandardItem):
    def __init__(self, geologicalMeasurementType):
        StandardItem.__init__(self, geologicalMeasurementType)
        self.showData()
