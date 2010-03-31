from PyQt4.QtGui import *
from PyQt4.QtCore import *

from PenSamplePixmap import *

class PenCapStyleSelector(QComboBox):
    styleChanged = pyqtSignal(Qt.PenCapStyle)
    def __init__(self, parent):
        QComboBox.__init__(self, parent)
        self.setToolTip(self.tr("Pen Cap Style"))
        self.pen = QPen()
        self.pen.setWidth(8)
        self.pen.setColor(Qt.black)
        self.currentIndexChanged.connect(self.onCurrentIndexChange)
        self.styles = dict()
        self.styles[0] = Qt.FlatCap
        self.styles[1] = Qt.SquareCap
        self.styles[2] = Qt.RoundCap
        self.reload()
    def onColorChange(self, color):
        self.pen.setColor(color)
        self.reload()
    def onPenWidthChange(self, w):
        self.pen.setWidth(w)
        self.reload()
    def reload(self):
        self.clear()
        self.insertItem(0, self.createSamplePixmapIcon(self.styles[0]), self.tr("Flat"), QVariant(0))
        self.insertItem(1, self.createSamplePixmapIcon(self.styles[1]), self.tr("Square"), QVariant(1))
        self.insertItem(2, self.createSamplePixmapIcon(self.styles[2]), self.tr("Round"), QVariant(2))
    def createSamplePixmapIcon(self, capStyle):
        self.pen.setCapStyle(capStyle)
        pm = PenSamplePixmap(10, 10)
        pm.drawSampleLine(self.pen)
        return QIcon(pm)
        
    def onCurrentIndexChange(self, idx):
        if idx < 0:
            return
        self.styleChanged.emit(self.styles[idx])
    def setPenCapStyle(self, style):
        for k,v in self.styles.iteritems():
            if v == style:
                self.setCurrentIndex(k)
