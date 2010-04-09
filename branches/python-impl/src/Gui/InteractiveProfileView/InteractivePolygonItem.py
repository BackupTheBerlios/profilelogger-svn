from PyQt4.QtGui import *
from PyQt4.QtCore import *

class InteractivePolygonItem(QGraphicsPolygonItem):
    def __init__(self, parent, scene,
                 polygon):
        QGraphicsPolygonItem.__init__(self, parent, scene)
        self.setPolygon(polygon)
