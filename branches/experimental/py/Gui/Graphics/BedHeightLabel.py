from GraphicsTextItem import GraphicsTextItem

class BedHeightLabel(GraphicsTextItem):
    def __init__(self, parent, scene, height):
        GraphicsTextItem.__init__(self, parent, scene)
        self.setText(QString(height))
