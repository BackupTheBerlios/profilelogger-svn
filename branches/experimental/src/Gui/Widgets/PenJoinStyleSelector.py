from PyQt4.QtGui import *
from PyQt4.QtCore import *

from PenSamplePixmap import *

class PenJoinStyleSelector(QComboBox):
    styleChanged = pyqtSignal(Qt.PenJoinStyle)
    def __init__(self, parent):
        QComboBox.__init__(self, parent)
        self.setToolTip(self.tr("Pen Join Style"))
        self.pen = QPen()
        self.pen.setWidth(8)
        self.pen.setColor(Qt.black)
        self.currentIndexChanged.connect(self.onCurrentIndexChange)
        self.styles = dict()
        self.styles[0] = Qt.BevelJoin
        self.styles[1] = Qt.MiterJoin
        self.styles[2] = Qt.RoundJoin
        self.reload()
    def onColorChange(self, color):
        self.pen.setColor(color)
        self.reload()
    def onPenWidthChange(self, w):
        self.pen.setWidth(w)
        self.reload()
    def reload(self):
        self.clear()
        self.insertItem(0, self.createSamplePixmapIcon(self.styles[0]), self.tr("Bevel"), QVariant(0))
        self.insertItem(1, self.createSamplePixmapIcon(self.styles[1]), self.tr("Miter"), QVariant(1))
        self.insertItem(2, self.createSamplePixmapIcon(self.styles[2]), self.tr("Round"), QVariant(2))
    def createSamplePixmapIcon(self, joinStyle):
        self.pen.setJoinStyle(joinStyle)
        pm = PenSamplePixmap(10, 10)
        pm.drawSampleLine(self.pen)
        return QIcon(pm)
        
    def onCurrentIndexChange(self, idx):
        if idx < 0:
            return
        self.styleChanged.emit(self.styles[idx])
    def setPenJoinStyle(self, style):
        for k,v in self.styles.iteritems():
            if v == style:
                self.setCurrentIndex(k)
