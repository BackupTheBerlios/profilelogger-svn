from PyQt4.QtGui import *
from PyQt4.QtCore import *

class PolygonItem(QGraphicsPolygonItem):
    def __init__(self, parent, scene, polygon=None):
        QGraphicsPolygonItem.__init__(self, parent, scene)
        if polygon is not None:
            self.setPolygon(polygon)
