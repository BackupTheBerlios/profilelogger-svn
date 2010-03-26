from PyQt4.QtGui import *
from PyQt4.QtCore import *

from Gui.Dialogs.DatabaseExceptionDialog import DatabaseExceptionDialog

from sqlalchemy.exc import *
from sqlalchemy.orm.exc import *

from StraightLineItem import *
from RectangleItem import *
from EllipseItem import *
from PolygonItem import *
from PainterPathItem import *

from Gui.Dialogs.DatabaseExceptionDialog import DatabaseExceptionDialog

from sqlalchemy.exc import *
from sqlalchemy.orm.exc import *

class CanvasScene(QGraphicsScene):
    currentItem = None
    currentPen = None
    currentBrush = None
    isDeleting = False
    isDrawing = False
    isEditing = False
    isMoving = False

    def __init__(self, parent):
        QGraphicsScene.__init__(self, parent)
        self.drawing = None
        self.drawHelpLines()
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
        if self.currentItem.__class__ == PainterPathItem:
            if self.currentItem.painterPath is not None:
                self.currentItem.painterPath.pen = self.currentPen
            return
        
    def onBrushChange(self, b):
        self.currentBrush = b
        if self.currentItem.__class__ == StraightLineItem:
            return
        if self.currentItem.__class__ == RectangleItem:
            if self.currentItem.rectangle is not None:
                self.currentItem.rectangle.brush = self.currentBrush
    def setDrawingMode(self):
        self.isDrawing = True
        self.isDeleting = False
        self.isEditing = False
        self.isMoving = False
    def setDeletingMode(self):
        self.isDrawing = False
        self.isDeleting = True
        self.isEditing = False
        self.isMoving = False
    def setEditingMode(self):
        self.isDrawing = False
        self.isDeleting = False
        self.isEditing = True
        self.isMoving = False
    def setMovingMode(self):
        self.isDrawing = False
        self.isDeleting = False
        self.isEditig = False
        self.isMoving = True
    def drawStraightLine(self):
        self.setDrawingMode()
        self.currentItem = StraightLineItem()
    def drawRectangle(self):
        self.setDrawingMode()
        self.currentItem = RectangleItem()
    def drawEllipse(self):
        self.setDrawingMode()
        self.currentItem = EllipseItem()
    def drawPolygon(self):
        self.setDrawingMode()
        self.currentItem = PolygonItem()
    def drawPainterPath(self):
        self.setDrawingMode()
        self.currentItem = PainterPathItem()
    def mousePressEvent(self, e):
        if Qt.LeftButton != e.button():
            e.ignore()
            return
        if self.isDrawing:
            self.beginDrawingAt(e.scenePos())
            return
        if self.isDeleting:
            self.deleteAt(e.scenePos())
            return
        if self.isEditing:
            self.editAt(e.scenePos())
            return
        if self.isMoving:
            self.beginMoveAt(e.scenePos())
    def deleteAt(self, pos):
        itm = self.itemAt(pos)
        if itm is None:
            return
        if itm.__class__ not in [StraightLineItem, RectangleItem, EllipseItem, PolygonItem, PainterPathItem]:
            return
        self.removeItem(itm)
        try:
            if itm.__class__ == StraightLineItem:
                QApplication.instance().db.session.delete(itm.straightLine)
            if itm.__class__ == RectangleItem:
                QApplication.instance().db.session.delete(itm.rectangle)
            if itm.__class__ == EllipseItem:
                QApplication.instance().db.session.delete(itm.ellipse)
            if itm.__class__ == PolygonItem:
                QApplication.instance().db.session.delete(itm.polygon)
            if itm.__class__ == PainterPathItem:
                QApplication.instance().db.session.delete(itm.painterPath)
            QApplication.instance().db.session.commit()
            return True
        except IntegrityError, e:
            dlg = DatabaseExceptionDialog(QApplication.activeWindow(), e)
            dlg.exec_()
            QApplication.instance().db.session.rollback()
        except ConcurrentModificationError, e:
            dlg = DatabaseExceptionDialog(QApplication.activeWindow(), e)
            dlg.exec_()
            QApplication.instance().db.session.rollback()
        except ProgrammingError, e:
            dlg = DatabaseExceptionDialog(QApplication.activeWindow(), e)
            dlg.exec_()
            QApplication.instance().db.session.rollback()
    def editAt(self, pos):
        pass
    def beginDrawingAt(self, scenePos):
        if self.currentItem.__class__ == StraightLineItem:
            self.beginStraightLine(scenePos)
        if self.currentItem.__class__ == RectangleItem:
            self.beginRectangle(scenePos)
        if self.currentItem.__class__ == EllipseItem:
            self.beginEllipse(scenePos)
        if self.currentItem.__class__ == PolygonItem:
            self.beginPolygon(scenePos)
        if self.currentItem.__class__ == PainterPathItem:
            self.beginPainterPath(scenePos)
        self.refresh()
    def beginMoveAt(self, scenePos):
        self.currentItem = self.itemAt(scenePos)
    def continueMoveAt(self, scenePos):
        if self.currentItem is not None:
            pass
    def finishMovingAt(self, scenePos):
        if self.currentItem is not None:
            pass
    def mouseMoveEvent(self, e):
        if self.isDrawing:
            self.continueDrawingAt(e.scenePos())
            e.accept()
            return
        if self.isMoving:
            self.continueMovingAt(e.scenePos())
            e.accept()
            return
        e.ignore()
    def continueDrawingAt(self, scenePos):
        if self.currentItem.__class__ == StraightLineItem:
            self.continueStraightLine(scenePos)
        if self.currentItem.__class__ == RectangleItem:
            self.continueRectangle(scenePos)
        if self.currentItem.__class__ == EllipseItem:
            self.continueEllipse(scenePos)
        if self.currentItem.__class__ == PolygonItem:
            self.continuePolygon(scenePos)
        if self.currentItem.__class__ == PainterPathItem:
            self.continuePainterPath(scenePos)
        self.refresh()
    def mouseReleaseEvent(self, e):
        if Qt.LeftButton != e.button():
            e.ignore()
            return;
        if self.isDrawing:
            self.finishDrawingAt(e.scenePos())
            e.accept()
            return
        if self.isMoving:
            self.finishMovingAt(e.scenePos())
            e.accept()
            return
        e.ignore()
        self.refresh()
    def finishDrawingAt(self, scenePos):
        if self.currentItem.__class__ == StraightLineItem:
            self.finishStraightLine(scenePos)
        if self.currentItem.__class__ == RectangleItem:
            self.finishRectangle(scenePos)
        if self.currentItem.__class__ == EllipseItem:
            self.finishEllipse(scenePos)
        if self.currentItem.__class__ == PolygonItem:
            self.finishPolygon(scenePos)
        if self.currentItem.__class__ == PainterPathItem:
            self.finishPainterPath(scenePos)
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
    def beginPainterPath(self, startPos):
        if not self.checkForPen():
            return
        self.currentItem.painterPath = PainterPath(None, self.drawing, 
                                                   startPos.x(), startPos.y(),
                                                   [],
                                                   self.currentPen)
        self.currentItem.painterPath.pen = self.currentPen
        self.currentItem.painterPath.brush = self.currentBrush
        self.addItem(self.currentItem)
        self.currentItem.updateFromData()
    def continuePainterPath(self, endPos):
        self.currentItem.painterPath.appendPoint(endPos.x() - self.currentItem.painterPath.posX,
                                                 endPos.y() - self.currentItem.painterPath.posY)
        self.currentItem.updateFromData()
    def finishPainterPath(self, endPos):
        self.currentItem.painterPath.appendPoint(endPos.x() - self.currentItem.painterPath.posX,
                                                 endPos.y() - self.currentItem.painterPath.posY) 
        self.currentItem.updateFromData()
        self.currentItem = None
        self.currentItem = PainterPathItem()
    def onEdit(self):
        self.setEditingMode()
    def onDelete(self):
        self.setDeletingMode()
    def onMove(self):
        self.setMovingMode()
    def drawHelpLines(self):
        patternHintRect = QGraphicsRectItem(0, 0, 150, 150)
        txt = QGraphicsTextItem(self.tr("Suggested Pattern Size"))
        txt.setPos(0, 0 - txt.boundingRect().height())
        pen = QPen(Qt.gray)
        pen.setStyle(Qt.DashLine)
        pen.setWidth(1)
        patternHintRect.setPen(pen)
        self.addItem(patternHintRect)
        self.addItem(txt)

        beddingHintRect = QGraphicsRectItem(0, 0, patternHintRect.rect().width() * 3, patternHintRect.rect().height())
        beddingHintRect.setPen(pen)
        txt2 = QGraphicsTextItem(self.tr("Suggested Bedding Type Pattern Size"))
        txt2.setPos(beddingHintRect.rect().width() - txt2.boundingRect().width(),
                    0 - txt2.boundingRect().height())
        self.addItem(beddingHintRect)
        self.addItem(txt2)

        x = 0
        while x < beddingHintRect.rect().width():
            p = QPen(Qt.gray)
            p.setWidth(1)
            p.setStyle(Qt.DotLine)
            l = QGraphicsLineItem(x, 0, x, beddingHintRect.rect().height())
            l.setPen(p)
            self.addItem(l)
            x += beddingHintRect.rect().width() / 30
        y = 0
        while y < beddingHintRect.rect().height():
            p = QPen(Qt.gray)
            p.setWidth(1)
            p.setStyle(Qt.DotLine)
            l = QGraphicsLineItem(0, y, beddingHintRect.rect().width(), y)
            l.setPen(p)
            self.addItem(l)
            y += beddingHintRect.rect().height() / 10
