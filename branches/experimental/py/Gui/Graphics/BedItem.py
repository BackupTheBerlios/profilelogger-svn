from GraphicsRectItem import GraphicsRectItem

class BedItem(GraphicsRectItem):
    def __init__(self, parent, scene, bed):
        GraphicsRectItem.__init__(self, parent, scene)
        self.bed = bed
