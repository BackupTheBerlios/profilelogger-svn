from PyQt4.QtGui import *
from PyQt4.QtCore import *

from BedItem import *

class SimpleProfile(QGraphicsRectItem):
    def __init__(self, parent, scene, 
                 profile, 
                 rect, pos, pen, 
                 columnWidths, columnSequence):
        QGraphicsRectItem.__init__(self, parent, scene)
        self.profile = profile
        self.columnWidths = columnWidths
        self.columnSequence = columnSequence
        self.headerItems = dict()
        self.setRect(rect)
        self.setPos(pos)
        self.setPen(pen)
        self.drawHeightMarks()
        self.drawBeds()
    def drawBeds(self):
        y = self.rect().height()
        for b in self.profile.beds:
            y -= self.scene().scaleMillimetresToPixel(b.heightInMillimetres())
            BedItem(self, self.scene(), b,
                    QRectF(0, 0, self.rect().width(),
                           self.scene().scaleLengthToPixel(b.height, b.lengthUnit)),
                    QPointF(0, y),
                    self.pen(),
                    self.columnWidths, self.columnSequence)
    def drawHeightMarks(self):
        self.drawSmallHeightMarks()
        self.drawBigHeightMarks()
    def drawSmallHeightMarks(self):
        height = self.profile.startHeightValue * self.profile.startHeightLengthUnit.microMetre / 1000
        y = self.rect().height()
        mmStep = self.profile.bigMarksDistanceValue * self.profile.bigMarksDistanceLengthUnit.microMetre / 1000
        pixelStep = self.scene().scaleMillimetresToPixel(mmStep)
        pos = QPointF(0, 0)
        for i in self.columnSequence:
            if i != HeightHeaderItem:
                x = pos.x()
                x += self.columnWidths[i]
                pos.setX(x)
            else:
                break
        f = QFont()
        f.setPointSize(9)
        while y > 0:
            pos.setY(y)
            mark = QGraphicsLineItem(QLineF(pos, QPointF(pos.x() + 10, pos.y())), self)
            lbl = QGraphicsTextItem(unicode(QString("%1").arg(height)), self)
            lbl.setFont(f)
            lbl.adjustSize()
            lbl.setPos(QPointF(pos.x() + 15, pos.y() - lbl.boundingRect().height() / 2))
            height += mmStep
            y -= pixelStep
    def drawBigHeightMarks(self):
        height = self.profile.startHeightValue * self.profile.startHeightLengthUnit.microMetre / 1000
        y = self.rect().height()
        mmStep = self.profile.smallMarksDistanceValue * self.profile.smallMarksDistanceLengthUnit.microMetre / 1000
        pixelStep = self.scene().scaleMillimetresToPixel(mmStep)
        pos = QPointF(0, 0)
        for i in self.columnSequence:
            if i != HeightHeaderItem:
                x = pos.x()
                x += self.columnWidths[i]
                pos.setX(x)
            else:
                break
        f = QFont()
        f.setPointSize(9)
        while y > 0:
            pos.setY(y)
            mark = QGraphicsLineItem(QLineF(pos, QPointF(pos.x() + 5, pos.y())), self)
            height += mmStep
            y -= pixelStep

