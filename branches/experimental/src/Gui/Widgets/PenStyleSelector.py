from PyQt4.QtGui import *
from PyQt4.QtCore import *

from PenSamplePixmap import *

class PenStyleSelector(QComboBox):
    styleChanged = pyqtSignal(Qt.PenStyle)
    def __init__(self, parent):
        QComboBox.__init__(self, parent)
        self.setToolTip(self.tr("Pen Style"))
        self.pen = QPen()
        self.pen.setWidth(8)
        self.pen.setColor(Qt.black)
        self.currentIndexChanged.connect(self.onCurrentIndexChange)
        self.styles = dict()
        self.styles[0] = Qt.SolidLine
        self.styles[1] = Qt.DashLine
        self.styles[2] = Qt.DotLine
        self.styles[3] = Qt.DashDotLine
        self.styles[4] = Qt.DashDotDotLine
        self.reload()
    def onColorChange(self, color):
        self.pen.setColor(color)
        self.reload()
    def onPenWidthChange(self, w):
        self.pen.setWidth(w)
        self.reload()
    def reload(self):
        self.clear()
        self.insertItem(0, self.createSamplePixmapIcon(self.styles[0]), self.tr("Solid"), QVariant(0))
        self.insertItem(1, self.createSamplePixmapIcon(self.styles[1]), self.tr("Dashed"), QVariant(1))
        self.insertItem(2, self.createSamplePixmapIcon(self.styles[2]), self.tr("Dotted"), QVariant(2))
        self.insertItem(3, self.createSamplePixmapIcon(self.styles[3]), self.tr("Dash-Dotted"), QVariant(3))
        self.insertItem(4, self.createSamplePixmapIcon(self.styles[4]), self.tr("Dash-Dotted-Dotted"), QVariant(4))
    def createSamplePixmapIcon(self, Style):
        self.pen.setStyle(Style)
        pm = PenSamplePixmap(10, 10)
        pm.drawSampleLine(self.pen)
        return QIcon(pm)
        
    def onCurrentIndexChange(self, idx):
        if idx < 0:
            return
        self.styleChanged.emit(self.styles[idx])
    def setPenStyle(self, style):
        for k,v in self.styles.iteritems():
            if v == style:
                self.setCurrentIndex(k)

