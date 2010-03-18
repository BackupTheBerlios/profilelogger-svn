from PyQt4.QtGui import *
from PyQt4.QtCore import *

from LineItem import LineItem

class CanvasScene(QGraphicsScene):
    def __init__(self, parent):
        QGraphicsScene.__init__(self, parent)
        self.currentItem = None
        self.currentTmpPen = QPen(Qt.blue)
        self.currentPen = QPen(Qt.black)
        self.isDeleting = False
    def drawStraightLine(self):
        self.isDeleting = False
        self.currentItem = LineItem(None, self, Qt.blue)
        self.currentItem.setPen(Qt.blue)
    def mousePressEvent(self, e):
        if e.button() != Qt.LeftButton:
            e.ignore()
            return
        if self.isDeleting:
            self.deleteObjectsAt(e.scenePos())
            return
        if self.currentItem.__class__ == LineItem:
            self.currentItem.setLine(QLineF(e.scenePos(), e.scenePos()))
            
    def mouseMoveEvent(self, e):
        if self.isDeleting:
            return
        if self.currentItem.__class__ == LineItem:
            l = self.currentItem.line()
            self.currentItem.setLine(QLineF(l.p1(), e.scenePos()))
    def mouseReleaseEvent(self, e):
        if e.button() != Qt.LeftButton:
            e.ignore()
            return
        if self.isDeleting:
            return
        if self.currentItem.__class__ == LineItem:
            l = self.currentItem.line()
            self.currentItem.setLine(QLineF(l.p1(), e.scenePos()))
            tmp = LineItem(None, self, Qt.black, self.currentItem.line())
            tmp.setPen(self.currentPen)
            self.removeItem(self.currentItem)
            self.drawStraightLine()
    def onPenWidthChange(self, w):
        self.currentPen.setWidth(w)
    def onPenColorChange(self, c):
        self.currentPen.setColor(c)
    def onDelete(self):
        self.isDeleting = True
    def deleteObjectsAt(self, pos):
        itm = self.itemAt(pos)
        while itm is not None:
            self.removeItem(itm)
            itm = self.itemAt(pos)
