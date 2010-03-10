from PyQt4.QtGui import *
from PyQt4.QtCore import *

from Gui.ItemModels.LengthUnitItemModel import LengthUnitItemModel
from Gui.ItemViews.LengthUnitItemView import LengthUnitItemView

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupMenu()
        self.setupStatusBar()

    def setupMenu(self):
        self.fileM = QMenu(self.tr('&File'), self.menuBar())
        self.dbM = QMenu(self.tr('&Database'), self.menuBar())

        for a in QApplication.instance().getFileActions():
            self.fileM.addAction(a)
        for a in QApplication.instance().getDatabaseActions():
            self.dbM.addAction(a)

        self.menuBar().addMenu(self.fileM)
        self.menuBar().addMenu(self.dbM)

    def setupStatusBar(self):
        self.dbStatusW = QLabel(self.statusBar())
        self.statusBar().addPermanentWidget(self.dbStatusW)
        self.dbStatusW.setText(self.tr('Not Connected'))
        QApplication.instance().databaseConnected.connect(self.onDatabaseConnected)

    def onDatabaseConnected(self, msg):
        self.dbStatusW.setText(msg)
        self.lengthUnitsW = LengthUnitItemView(self, QApplication.instance().lengthUnitModel)
        self.setCentralWidget(self.lengthUnitsW)
