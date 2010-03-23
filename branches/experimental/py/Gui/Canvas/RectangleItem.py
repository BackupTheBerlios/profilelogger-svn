from PyQt4.QtCore import *
from PyQt4.QtGui import *

from Model.Rectangle import *

class RectangleItem(QGraphicsRectItem):
    def __init__(self, rectangle=None):
        QGraphicsRectItem.__init__(self)
        self.rectangle = rectangle
        self.updateFromData()
    def hasRectangle(self):
        return self.rectangle is not None
    def updateFromData(self):
        if not self.hasRectangle():
            return
        self.setRect(self.rectangle.makeRect())
        if self.rectangle.hasPen():
            self.setPen(self.rectangle.pen.getQPen())
        if self.rectangle.hasBrush():
            self.setBrush(self.rectangle.brush.getQBrush())
        self.setPos(self.rectangle.makePosition())
