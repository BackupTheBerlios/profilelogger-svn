from PyQt4.QtGui import *
from PyQt4.QtCore import *

from PenSamplePixmap import *

class BrushStyleSelector(QComboBox):
    styleChanged = pyqtSignal(Qt.BrushStyle)
    def __init__(self, parent):
        QComboBox.__init__(self, parent)
        self.setToolTip(self.tr("Brush Style"))
        self.pen = QPen()
        self.pen.setWidth(8)
        self.pen.setColor(Qt.black)
        self.currentIndexChanged.connect(self.onCurrentIndexChange)
        self.styles = dict()
        self.styles[0] = Qt.SolidPattern
        self.styles[1] = Qt.Dense1Pattern
        self.styles[2] = Qt.Dense2Pattern
        self.styles[3] = Qt.Dense3Pattern
        self.styles[4] = Qt.Dense4Pattern
        self.styles[5] = Qt.Dense5Pattern
        self.styles[6] = Qt.Dense6Pattern
        self.styles[7] = Qt.Dense7Pattern
        self.styles[8] = Qt.NoBrush
        self.styles[9] = Qt.HorPattern
        self.styles[10] = Qt.VerPattern
        self.styles[11] = Qt.CrossPattern
        self.styles[12] = Qt.BDiagPattern
        self.styles[13] = Qt.FDiagPattern
        self.styles[14] = Qt.DiagCrossPattern
#        self.styles[15] = Qt.LinearGradientPattern
#        self.styles[16] = Qt.RadialGradientPattern
#        self.styles[17] = Qt.ConicalGradientPattern
        self.reload()
    def onColorChange(self, color):
        self.pen.brush().setColor(color)
        self.pen.setColor(color)
        self.reload()
    def onPenWidthChange(self, w):
        self.pen.setWidth(w)
        self.reload()
    def reload(self):
        self.clear()
        self.insertItem(0, self.createSamplePixmapIcon(self.styles[0]), self.tr("Solid"), QVariant(0))
        self.insertItem(1, self.createSamplePixmapIcon(self.styles[1]), self.tr("Dense 1"), QVariant(1))
        self.insertItem(2, self.createSamplePixmapIcon(self.styles[2]), self.tr("Dense 2"), QVariant(2))
        self.insertItem(3, self.createSamplePixmapIcon(self.styles[3]), self.tr("Dense 3"), QVariant(3))
        self.insertItem(4, self.createSamplePixmapIcon(self.styles[4]), self.tr("Dense 4"), QVariant(4))
        self.insertItem(5, self.createSamplePixmapIcon(self.styles[5]), self.tr("Dense 5"), QVariant(5))
        self.insertItem(6, self.createSamplePixmapIcon(self.styles[6]), self.tr("Dense 6"), QVariant(6))
        self.insertItem(7, self.createSamplePixmapIcon(self.styles[7]), self.tr("Dense 7"), QVariant(7))
        self.insertItem(8, self.createSamplePixmapIcon(self.styles[8]), self.tr("No Brush"), QVariant(8))
        self.insertItem(9, self.createSamplePixmapIcon(self.styles[9]), self.tr("Horizontal"), QVariant(9))
        self.insertItem(10, self.createSamplePixmapIcon(self.styles[10]), self.tr("Vertical"), QVariant(10))
        self.insertItem(11, self.createSamplePixmapIcon(self.styles[11]), self.tr("Cross"), QVariant(11))
        self.insertItem(12, self.createSamplePixmapIcon(self.styles[12]), self.tr("Right Diagonal"), QVariant(12))
        self.insertItem(13, self.createSamplePixmapIcon(self.styles[13]), self.tr("Left Diagonal"), QVariant(13))
        self.insertItem(14, self.createSamplePixmapIcon(self.styles[14]), self.tr("Diagonal Cross"), QVariant(14))
#        self.insertItem(15, self.createSamplePixmapIcon(self.styles[15]), self.tr("Linear Gradient"), QVariant(15))
 #       self.insertItem(16, self.createSamplePixmapIcon(self.styles[16]), self.tr("Radial Gradient"), QVariant(16))
  #      self.insertItem(17, self.createSamplePixmapIcon(self.styles[17]), self.tr("Conical Gradient"), QVariant(17))
    def createSamplePixmapIcon(self, Style):
        self.pen.brush().setStyle(Style)
        pm = PenSamplePixmap(50, 50)
        pm.fillWithBrush(self.pen.brush())
        return QIcon(pm)
        
    def onCurrentIndexChange(self, idx):
        if idx < 0:
            return
        self.styleChanged.emit(self.styles[idx])
    def setBrushStyle(self, style):
        for k,v in self.styles.iteritems():
            if v == style:
                self.setCurrentIndex(k)

