from PyQt4.QtGui import *
from PyQt4.QtCore import *

class ColorSelectionWidget(QWidget):
    colorChanged = pyqtSignal(QColor)

    def __init__(self, parent, label=None, color=None):
        QWidget.__init__(self, parent)
        self.currentColor = color
        self.setLayout(QHBoxLayout(self))
        if label is not None:
            self.layout().addWidget(QLabel(label, self))
        self.pixmap = QPixmap(20, 20)
        self.displayW = QLabel(self)
        self.browseW = QPushButton(self.tr("..."), self)
        self.layout().addWidget(self.displayW)
        self.layout().addWidget(self.browseW)
        self.browseW.clicked.connect(self.onBrowse)
        self.showColor()
    def showColor(self):
        self.pixmap.fill(self.currentColor)
        self.displayW.setPixmap(self.pixmap)
    def onBrowse(self):
        dlg = QColorDialog(self)
        dlg.setCurrentColor(self.currentColor)
        if QDialog.Accepted == dlg.exec_():
            self.currentColor = dlg.selectedColor()
            self.showColor()
            self.colorChanged.emit(self.currentColor)
