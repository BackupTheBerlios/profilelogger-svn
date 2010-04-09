from PyQt4.QtCore import *
from PyQt4.QtGui import *

class LegendItem(QGraphicsRectItem):
    def __init__(self, parent, scene,
                 rect, pen, font,
                 dataset):
        QGraphicsRectItem.__init__(self, parent, scene)
        self.setRect(rect)
        self.setPen(pen)
        self.font = font
        self.dataset = dataset
