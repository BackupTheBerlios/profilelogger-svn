from PyQt4.QtGui import *
from PyQt4.QtCore import *

from FilledRectInBed import *

class GrainSizeItem(FilledRectInBed):
    def __init__(self, parent, scene,
                 rect, pen,
                 bed):
        FilledRectInBed.__init__(self, parent, scene,
                                 rect, pen,
                                 bed)
        if len(parent.bed.grainSizes) > 0:
            self.drawGrainSizes(parent.bed.grainSizes)
    def drawGrainSizes(self, itmList):
        if len(itmList) == 1:
            self.drawRectangularEntry(itmList[0])
        else:
            self.drawPolygonalEntry(itmList)
    def drawRectangularEntry(self, grainSizeInBed):
        rect = QRectF(QPointF(0, 
                              self.rect().height() - self.rect().height() * grainSizeInBed.end / 100),
                      QPointF(self.rect().width() * grainSizeInBed.grainSize.percentFromMinimum / 100,
                              self.rect().height() - self.rect().height() * grainSizeInBed.begin / 100))
        r = QGraphicsRectItem(rect, self, self.scene())
    def drawPolygonalEntry(self, lst):
        bottomLeft = QPointF(0, self.rect().height())
        topLeft = QPointF(0, 0)
        pointLst = []
        
        isFirst = False
        lastX = 0.0
        for i in lst:
            topLeft.setY(self.yFromBedPercent(i.end))

            if isFirst:
                lastX = self.xFromGrainSize(i.grainSize)
                isFirst = False

                pointLst.append(QPointF(0, self.yFromBedPercent(i.begin)))
                pointLst.append(QPointF(lastX, self.yFromBedPercent(i.begin)))
                pointLst.append(QPointF(lastX, self.yFromBedPercent(i.end)))
            else:
                x = self.xFromGrainSize(i.grainSize)
                if x < lastX:
                    lastX = x
                    pointLst.append(QPointF(lastX, self.yFromBedPercent(i.begin)))
                    pointLst.append(QPointF(lastX, self.yFromBedPercent(i.end)))
                if x == lastX:
                    pointLst.append(QPointF(lastX, self.yFromBedPercent(i.end)))
                if x > lastX:
                    lastX = x
                    pointLst.append(QPointF(lastX, self.yFromBedPercent(i.begin)))
                    pointLst.append(QPointF(lastX, self.yFromBedPercent(i.end)))

        poly = QPolygonF()
        poly.append(bottomLeft)
        for i in pointLst:
            poly.append(i)
        poly.append(topLeft)
        itm = QGraphicsPolygonItem(poly, self, self.scene())
    def xFromGrainSize(self, grainSize):
        return self.rect().width() * grainSize.percentFromMinimum / 100
    def yFromBedPercent(self, percent):
        return self.rect().height() - self.rect().height() * percent / 100
