from PyQt4.QtGui import *
from PyQt4.QtCore import *

class GrainSizePolygonItem(QGraphicsPolygonItem):
    def __init__(self, parent, scene,
                 polygon, pen,
                 bed):
        QGraphicsPolygonItem.__init__(self, parent, scene)
        self.setPolygon(polygon)
        self.setPen(Qt.black),
        self.bed = bed
