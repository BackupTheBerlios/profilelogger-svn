from PyQt4.QtGui import *
from PyQt4.QtCore import *

from LineItem import LineItem
from RectItem import RectItem
from PolygonItem import PolygonItem
from EllipseItem import EllipseItem
from PathItem import PathItem

from LineItemEditorDialog import *
from PolygonItemEditorDialog import *
from RectItemEditorDialog import *
from EllipseItemEditorDialog import *
from PathItemEditorDialog import *

class CanvasScene(QGraphicsScene):
    def __init__(self, parent):
        QGraphicsScene.__init__(self, parent)
        self.currentItem = None
        self.currentTmpPen = QPen(Qt.blue)
        self.currentPen = QPen(Qt.black)
        self.currentBrush = QBrush()
        self.currentBrush.setStyle(Qt.NoBrush)
        self.currentBrush.setColor(Qt.white)
        self.isDeleting = False
        self.isEditing = False
        self.isMoving = False
        self.isDrawing = False
        self.movingItm = None
    def setStateDeleting(self):
        self.isDeleting = True
        self.isEditing = False
        self.isMoving = False
        self.isDrawing = False
    def setStateEditing(self):
        self.isDeleting = False
        self.isEditing = True
        self.isMoving = False
        self.isDrawing = False
    def setStateMoving(self):
        self.isDeleting = False
        self.isEditing = False
        self.isMoving = True
        self.isDrawing = False
    def setStateDrawing(self):
        self.isDeleting = False
        self.isEditing = False
        self.isMoving = False
        self.isDrawing = True
    def drawStraightLine(self):
        self.setStateDrawing()
        self.currentItem = LineItem(None, self)
        self.currentItem.setPen(self.currentTmpPen)
    def drawRectangle(self):
        self.setStateDrawing()
        self.currentItem = RectItem(None, self)
        self.currentItem.setPen(self.currentTmpPen)
    def drawEllipse(self):
        self.setStateDrawing()
        self.currentItem = EllipseItem(None, self)
        self.currentItem.setPen(self.currentTmpPen)
    def drawPolygon(self):
        self.setStateDrawing()
        self.currentItem = PolygonItem(None, self)
        self.currentItem.setPen(self.currentTmpPen)
    def drawPath(self):
        self.setStateDrawing()
        self.currentItem = PathItem(None, self)
        self.currentItem.setPen(self.currentTmpPen)
    def mousePressEvent(self, e):
        if e.button() != Qt.LeftButton:
            e.ignore()
            return
        if self.isDeleting:
            self.deleteObjectsAt(e.scenePos())
            return
        if self.isEditing:
            self.editTopObjectAt(e.scenePos())
            return
        if self.isMoving:
            self.beginMove(e.scenePos())
            return
        if self.currentItem.__class__ == LineItem:
            self.currentItem.setLine(QLineF(e.scenePos(), e.scenePos()))
            return
        if self.currentItem.__class__ == RectItem:
            self.currentItem.setRect(QRectF(e.scenePos(), e.scenePos()))
            return
        if self.currentItem.__class__ == EllipseItem:
            self.currentItem.setRect(QRectF(e.scenePos(), e.scenePos()))
            return
        if self.currentItem.__class__ == PolygonItem:
            self.currentItem.setPolygon(QPolygonF())
            self.currentItem.polygon().append(e.scenePos())
            return
        if self.currentItem.__class__ == PathItem:
            p = QPainterPath()
            p.moveTo(e.scenePos())
            self.currentItem.setPath(p)
    def mouseMoveEvent(self, e):
        if self.isDeleting:
            return
        if self.isEditing:
            return
        if self.isMoving:
            self.continueMove(e.scenePos())
            return
        if self.currentItem.__class__ == LineItem:
            l = self.currentItem.line()
            self.currentItem.setLine(QLineF(l.p1(), e.scenePos()))
            return
        if self.currentItem.__class__ == RectItem:
            r = self.currentItem.rect()
            self.currentItem.setRect(QRectF(r.topLeft(), e.scenePos()))
            return
        if self.currentItem.__class__ == EllipseItem:
            r = self.currentItem.rect()
            self.currentItem.setRect(QRectF(r.topLeft(), e.scenePos()))
            return
        if self.currentItem.__class__ == PolygonItem:
            p = self.currentItem.polygon()
            p.append(e.scenePos())
            self.currentItem.setPolygon(p)
            return
        if self.currentItem.__class__ == PathItem:
            p = self.currentItem.path()
            p.lineTo(e.scenePos())
            self.currentItem.setPath(p)
            return
    def mouseReleaseEvent(self, e):
        if e.button() != Qt.LeftButton:
            e.ignore()
            return
        if self.isDeleting:
            return
        if self.isEditing:
            return
        if self.isMoving:
            self.endMove(e.scenePos())
            return
        self.drawAndSaveCurrentItem()
    def onPenWidthChange(self, w):
        self.currentPen.setWidth(w)
    def onPenColorChange(self, c):
        self.currentPen.setColor(c)
    def onDelete(self):
        self.setStateDeleting()
    def onEdit(self):
        self.setStateEditing()
    def onMove(self):
        self.setStateMoving()
    def deleteObjectsAt(self, pos):
        itm = self.itemAt(pos)
        while itm is not None:
            self.removeItem(itm)
            itm = self.itemAt(pos)
    def editTopObjectAt(self, pos):
        itm = self.itemAt(pos)
        if itm is None:
            return
        if itm.__class__ == LineItem:
            self.editLineItem(itm)
            return
        if itm.__class__ == PolygonItem:
            self.editPolygonItem(itm)
            return
        if itm.__class__ == RectItem:
            self.editRectItem(itm)
            return
        if itm.__class__ == EllipseItem:
            self.editEllipseItem(itm)
            return
        if itm.__class__ == PathItem:
            self.editPathItem(itm)
            return
    def editLineItem(self, itm):
        dlg = LineItemEditorDialog(None, itm)
        if dlg.exec_() == QDialog.Accepted:
            p = itm.pen()
            p.setWidth(dlg.penWidth)
            p.setColor(dlg.penColor)
            p.setCapStyle(dlg.penCapStyle)
            p.setJoinStyle(dlg.penJoinStyle)
            p.setStyle(dlg.penStyle)
            itm.setPen(p)
            self.refresh()
    def editPolygonItem(self, itm):
        dlg = PolygonItemEditorDialog(None, itm)
        if dlg.exec_() == QDialog.Accepted:
            p = itm.pen()
            b = itm.brush()
            p.setWidth(dlg.penWidth)
            p.setColor(dlg.penColor)
            p.setCapStyle(dlg.penCapStyle)
            p.setJoinStyle(dlg.penJoinStyle)
            p.setStyle(dlg.penStyle)
            b.setColor(dlg.brushColor)
            b.setStyle(dlg.brushStyle)
            itm.setPen(p)
            itm.setBrush(b)
            self.refresh()
    def editRectItem(self, itm):
        dlg = RectItemEditorDialog(None, itm)
        if dlg.exec_() == QDialog.Accepted:
            p = itm.pen()
            b = itm.brush()
            p.setWidth(dlg.penWidth)
            p.setColor(dlg.penColor)
            p.setCapStyle(dlg.penCapStyle)
            p.setJoinStyle(dlg.penJoinStyle)
            p.setStyle(dlg.penStyle)
            b.setColor(dlg.brushColor)
            b.setStyle(dlg.brushStyle)
            itm.setPen(p)
            itm.setBrush(b)
            self.refresh()
    def editPathItem(self, itm):
        dlg = PathItemEditorDialog(None, itm)
        if dlg.exec_() == QDialog.Accepted:
            p = itm.pen()
            b = itm.brush()
            p.setWidth(dlg.penWidth)
            p.setColor(dlg.penColor)
            p.setCapStyle(dlg.penCapStyle)
            p.setJoinStyle(dlg.penJoinStyle)
            p.setStyle(dlg.penStyle)
            b.setColor(dlg.brushColor)
            b.setStyle(dlg.brushStyle)
            itm.setPen(p)
            itm.setBrush(b)
            self.refresh()
    def editEllipseItem(self, itm):
        dlg = EllipseItemEditorDialog(None, itm)
        if dlg.exec_() == QDialog.Accepted:
            p = itm.pen()
            b = itm.brush()
            p.setWidth(dlg.penWidth)
            p.setColor(dlg.penColor)
            p.setCapStyle(dlg.penCapStyle)
            p.setJoinStyle(dlg.penJoinStyle)
            p.setStyle(dlg.penStyle)
            b.setColor(dlg.brushColor)
            b.setStyle(dlg.brushStyle)
            itm.setPen(p)
            itm.setBrush(b)
            self.refresh()

    def refresh(self):
        self.update(self.sceneRect())
    def onPenCapStyleChange(self, s):
        self.currentPen.setCapStyle(s)
    def onPenJoinStyleChange(self, s):
        self.currentPen.setJoinStyle(s)
    def onPenStyleChange(self, s):
        self.currentPen.setStyle(s)
    def onBrushColorChange(self, c):
        self.currentBrush.setColor(c)
    def onBrushStyleChange(self, s):
        self.currentBrush.setStyle(s)
    def beginMove(self, pos):
        print "moving todo"
    def continueMove(self, pos):
        print "moving todo"
    def endMove(self, pos):
        print "moving todo"
    def drawAndSaveCurrentItem(self):
        if self.currentItem.__class__ == LineItem:
            l = self.currentItem.line()
            self.currentItem.setLine(QLineF(l.p1(), e.scenePos()))
            tmp = LineItem(None, self, self.currentItem.line())
            tmp.setPen(self.currentPen)
            self.removeItem(self.currentItem)
            self.drawStraightLine()
            return
        if self.currentItem.__class__ == RectItem:
            r = self.currentItem.rect()
            self.currentItem.setRect(QRectF(r.topLeft(), e.scenePos()))
            tmp = RectItem(None, self, self.currentItem.rect())
            tmp.setPen(self.currentPen)
            tmp.setBrush(self.currentBrush)
            self.removeItem(self.currentItem)
            self.drawRectangle()
            return
        if self.currentItem.__class__ == EllipseItem:
            r = self.currentItem.rect()
            self.currentItem.setRect(QRectF(r.topLeft(), e.scenePos()))
            tmp = EllipseItem(None, self, self.currentItem.rect())
            tmp.setPen(self.currentPen)
            tmp.setBrush(self.currentBrush)
            self.removeItem(self.currentItem)
            self.drawEllipse()
            return
        if self.currentItem.__class__ == PolygonItem:
            p = self.currentItem.polygon()
            p.append(e.scenePos())
            tmp = PolygonItem(None, self, self.currentItem.polygon())
            tmp.setPen(self.currentPen)
            tmp.setBrush(self.currentBrush)
            self.removeItem(self.currentItem)
            self.drawPolygon()
        if self.currentItem.__class__ == PathItem:
            p = self.currentItem.path()
            p.lineTo(e.scenePos())
            tmp = PathItem(None, self, self.currentItem.path())
            tmp.setPen(self.currentPen)
            tmp.setBrush(self.currentBrush)
            self.removeItem(self.currentItem)
            self.drawPath()
