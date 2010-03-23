from PyQt4.QtGui import *
from PyQt4.QtCore import *

from Gui.Dialogs.DatabaseExceptionDialog import DatabaseExceptionDialog

from sqlalchemy.exc import *
from sqlalchemy.orm.exc import *

from StraightLineItem import *

class CanvasScene(QGraphicsScene):
    currentItem = None
    currentPen = None
    currentBrush = None
    def __init__(self, parent):
        QGraphicsScene.__init__(self, parent)
        self.drawing = None
    def onPenChange(self, p):
        self.currentPen = p
        if self.currentItem.__class__ == StraightLineItem:
            if self.currentItem.straightLine is not None:
                self.currentItem.straightLine.pen = self.currentPen
    def onBrushChange(self, b):
        self.currentBrush = b
        if self.currentItem.__class__ == StraightLineItem:
            pass
    def drawStraightLine(self):
        self.currentItem = StraightLineItem()
    def mousePressEvent(self, e):
        if Qt.LeftButton != e.button():
            e.ignore()
            return
        if self.currentItem.__class__ == StraightLineItem:
            if self.currentPen is None:
                QMessageBox.information(QApplication.activeWindow(),
                                        self.tr("Usage hint"),
                                        self.tr("<p>Pen required.</p>"))
                return
            self.currentItem.straightLine = StraightLine(None, self.drawing, 
                                                         e.scenePos().x(), e.scenePos().y(), 
                                                         e.scenePos().x(), e.scenePos().y(), 
                                                         self.currentPen)
            self.currentItem.straightLine.pen = self.currentPen
            self.addItem(self.currentItem)
            self.currentItem.updateFromData()
    def mouseMoveEvent(self, e):
        if self.currentItem.__class__ == StraightLineItem:
            self.currentItem.straightLine.x2 = e.scenePos().x()
            self.currentItem.straightLine.y2 = e.scenePos().y()
            print "pos: ", e.scenePos()
            self.currentItem.updateFromData()
    def mouseReleaseEvent(self, e):
        if Qt.LeftButton != e.button():
            e.ignore()
            return;
        if self.currentItem.__class__ == StraightLineItem:
            self.currentItem.straightLine.x2 = e.scenePos().x()
            self.currentItem.straightLine.y2 = e.scenePos().y()
            self.currentItem.updateFromData()
            self.currentItem = None
            self.currentItem = StraightLineItem()
