from StandardItem import StandardItem

class GeologicalMeasurementInBedItem(StandardItem):
    def __init__(self, geologicalMeasurementInBed):
        StandardItem.__init__(self, geologicalMeasurementInBed)
        self.showData()
