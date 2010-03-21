from PyQt4.QtGui import *
from PyQt4.QtCore import *

class PenSamplePixmap(QPixmap):
    def __init__(self, w=20, h=20):
        QPixmap.__init__(self, w, h)
    def drawSampleLine(self, pen):
        l = QLineF(0, self.height() / 2, self.width() * 0.8, self.height() / 2)
        self.fill(Qt.white)
        ptr = QPainter()
        ptr.begin(self)
        ptr.setPen(pen)
        ptr.drawLine(l)
        ptr.end()
    def fillWithBrush(self, brush):
        r = QRectF(0, 0, self.width(), self.height())
        p = QPen()
        p.setColor(brush.color())
        p.setBrush(brush)
        ptr = QPainter()
        ptr.begin(self)
        ptr.setPen(p)
        ptr.drawRect(r)
        ptr.end()
