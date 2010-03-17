from GraphicsRectItem import GraphicsRectItem

class PatternRect(QGraphicsRectItem):
    def __init__(self, parent, scene, brush):
        GraphicsRectItem.__init__(self, parent, scene)
        self.setBrush(brush)
