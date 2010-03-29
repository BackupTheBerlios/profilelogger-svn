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
        self.drawGrainSizes(parent.bed.grainSizes)
    def drawGrainSizes(self, lst):
        bottomLeft = QPointF(0, self.yFromBedPercent(lst[0].begin))
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
