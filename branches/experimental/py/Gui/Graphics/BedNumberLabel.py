from GraphicsTextItem import *

class BedNumberLabel(GraphicsTextItem):
    def __init__(self, parent, scene, number):
        GraphicsTextItem.__init__(self, parent, scene)
        self.setText(QString(number))
