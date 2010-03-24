from PyQt4.QtGui import *
from PyQt4.QtCore import *

from Gui.Dialogs.DatabaseExceptionDialog import DatabaseExceptionDialog

from sqlalchemy.exc import *
from sqlalchemy.orm.exc import *

from StraightLineItem import *
from RectangleItem import *
from EllipseItem import *
from PolygonItem import *

class CanvasScene(QGraphicsScene):
    currentItem = None
    currentPen = None
    currentBrush = None
    def __init__(self, parent):
        QGraphicsScene.__init__(self, parent)
        self.drawing = None
    def refresh(self):
        self.update(self.sceneRect())
    def checkForPen(self):
        if self.currentPen is None:
            QMessageBox.information(QApplication.activeWindow(),
                                    self.tr("Usage hint"),
                                    self.tr("<p>Pen required.</p>"))
            return False
        return True
    def onPenChange(self, p):
        self.currentPen = p
        if self.currentItem.__class__ == StraightLineItem:
            if self.currentItem.straightLine is not None:
                self.currentItem.straightLine.pen = self.currentPen
            return
        if self.currentItem.__class__ == RectangleItem:
            if self.currentItem.rectangle is not None:
                self.currentItem.rectangle.pen = self.currentPen
            return
        if self.currentItem.__class__ == EllipseItem:
            if self.currentItem.ellipse is not None:
                self.currentItem.ellipse.pen = self.currentPen
            return
        if self.currentItem.__class__ == PolygonItem:
            if self.currentItem.polygon is not None:
                self.currentItem.polygon.pen = self.currentPen
            return
        
    def onBrushChange(self, b):
        self.currentBrush = b
        if self.currentItem.__class__ == StraightLineItem:
            return
        if self.currentItem.__class__ == RectangleItem:
            if self.currentItem.rectangle is not None:
                self.currentItem.rectangle.brush = self.currentBrush
    def drawStraightLine(self):
        self.currentItem = StraightLineItem()
    def drawRectangle(self):
        self.currentItem = RectangleItem()
    def drawEllipse(self):
        self.currentItem = EllipseItem()
    def drawPolygon(self):
        self.currentItem = PolygonItem()
    def mousePressEvent(self, e):
        if Qt.LeftButton != e.button():
            e.ignore()
            return
        if self.currentItem.__class__ == StraightLineItem:
            self.beginStraightLine(e.scenePos())
        if self.currentItem.__class__ == RectangleItem:
            self.beginRectangle(e.scenePos())
        if self.currentItem.__class__ == EllipseItem:
            self.beginEllipse(e.scenePos())
        if self.currentItem.__class__ == PolygonItem:
            self.beginPolygon(e.scenePos())
        self.refresh()
    def mouseMoveEvent(self, e):
        if self.currentItem.__class__ == StraightLineItem:
            self.continueStraightLine(e.scenePos())
        if self.currentItem.__class__ == RectangleItem:
            self.continueRectangle(e.scenePos())
        if self.currentItem.__class__ == EllipseItem:
            self.continueEllipse(e.scenePos())
        if self.currentItem.__class__ == PolygonItem:
            self.continuePolygon(e.scenePos())

        self.refresh()
    def mouseReleaseEvent(self, e):
        if Qt.LeftButton != e.button():
            e.ignore()
            return;
        if self.currentItem.__class__ == StraightLineItem:
            self.finishStraightLine(e.scenePos())
        if self.currentItem.__class__ == RectangleItem:
            self.finishRectangle(e.scenePos())
        if self.currentItem.__class__ == EllipseItem:
            self.finishEllipse(e.scenePos())
        if self.currentItem.__class__ == PolygonItem:
            self.finishPolygon(e.scenePos())
    def beginStraightLine(self, startPos):
        if not self.checkForPen():
            return
        self.currentItem.straightLine = StraightLine(None, self.drawing, 
                                                     startPos.x(), startPos.y(), 
                                                     startPos.x(), startPos.y(), 
                                                     self.currentPen)
        self.currentItem.straightLine.pen = self.currentPen
        self.addItem(self.currentItem)
        self.currentItem.updateFromData()
    def continueStraightLine(self, endPos):
        self.currentItem.straightLine.x2 = endPos.x()
        self.currentItem.straightLine.y2 = endPos.y()
        self.currentItem.updateFromData()
    def finishStraightLine(self, endPos):
        self.currentItem.straightLine.x2 = endPos.x()
        self.currentItem.straightLine.y2 = endPos.y()
        self.currentItem.updateFromData()
        self.currentItem = None
        self.currentItem = StraightLineItem()
    def beginRectangle(self, startPos):
        if not self.checkForPen():
            return
        self.currentItem.rectangle = Rectangle(None, self.drawing, 
                                               startPos.x(), startPos.y(),
                                               0, 0, 
                                               0, 0, 
                                               self.currentPen)
        self.currentItem.rectangle.pen = self.currentPen
        self.currentItem.rectangle.brush = self.currentBrush
        self.addItem(self.currentItem)
        self.currentItem.updateFromData()
    def continueRectangle(self, endPos):
        self.currentItem.rectangle.x2 = endPos.x() - self.currentItem.rectangle.posX
        self.currentItem.rectangle.y2 = endPos.y() - self.currentItem.rectangle.posY
        self.currentItem.updateFromData()
    def finishRectangle(self, endPos):
        self.currentItem.rectangle.x2 = endPos.x() - self.currentItem.rectangle.posX
        self.currentItem.rectangle.y2 = endPos.y() - self.currentItem.rectangle.posY 
        self.currentItem.updateFromData()
        self.currentItem = None
        self.currentItem = RectangleItem()
    def beginEllipse(self, startPos):
        if not self.checkForPen():
            return
        self.currentItem.ellipse = Ellipse(None, self.drawing, 
                                           startPos.x(), startPos.y(),
                                           0, 0, 
                                           0, 0, 
                                           self.currentPen)
        self.currentItem.ellipse.pen = self.currentPen
        self.currentItem.ellipse.brush = self.currentBrush
        self.addItem(self.currentItem)
        self.currentItem.updateFromData()
    def continueEllipse(self, endPos):
        self.currentItem.ellipse.x2 = endPos.x() - self.currentItem.ellipse.posX
        self.currentItem.ellipse.y2 = endPos.y() - self.currentItem.ellipse.posY
        self.currentItem.updateFromData()
    def finishEllipse(self, endPos):
        self.currentItem.ellipse.x2 = endPos.x() - self.currentItem.ellipse.posX
        self.currentItem.ellipse.y2 = endPos.y() - self.currentItem.ellipse.posY 
        self.currentItem.updateFromData()
        self.currentItem = None
        self.currentItem = EllipseItem()
    def beginPolygon(self, startPos):
        if not self.checkForPen():
            return
        self.currentItem.polygon = Polygon(None, self.drawing, 
                                           startPos.x(), startPos.y(),
                                           [],
                                           self.currentPen)
        self.currentItem.polygon.pen = self.currentPen
        self.currentItem.polygon.brush = self.currentBrush
        self.addItem(self.currentItem)
        self.currentItem.updateFromData()
    def continuePolygon(self, endPos):
        self.currentItem.polygon.appendPoint(endPos.x() - self.currentItem.polygon.posX,
                                             endPos.y() - self.currentItem.polygon.posY)
        self.currentItem.updateFromData()
    def finishPolygon(self, endPos):
        self.currentItem.polygon.appendPoint(endPos.x() - self.currentItem.polygon.posX,
                                             endPos.y() - self.currentItem.polygon.posY) 
        self.currentItem.updateFromData()
        self.currentItem = None
        self.currentItem = PolygonItem()
        
        
