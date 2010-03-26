from PyQt4.QtGui import *
from PyQt4.QtCore import *

class BedNumberText(QGraphicsTextItem):
    def __init__(self, parent, scene, font, bed, lblAngle):
        QGraphicsTextItem.__init__(self, unicode(QString("%1").arg(bed.number, 5, 10, QChar('0'))), parent)
        self.setFont(font)
        self.setRotation(lblAngle)
        self.adjustSize()
