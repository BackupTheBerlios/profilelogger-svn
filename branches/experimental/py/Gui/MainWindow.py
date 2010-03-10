from PyQt4.QtGui import *
from PyQt4.QtCore import *

from Gui.ItemModels.LengthUnitItemModel import LengthUnitItemModel
from Gui.ItemViews.LengthUnitItemView import LengthUnitItemView

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupMenu()
        self.setupStatusBar()
        self.setupCentralWidget()
        QApplication.instance().databaseConnected.connect(self.onDatabaseConnected)
    def setupCentralWidget(self):
        self.setCentralWidget(QSplitter(Qt.Horizontal, self))
        self.setupGlobalTools()
        self.centralWidget().setEnabled(False)
    def setupGlobalTools(self):
        self.globalToolsW = QToolBox(self.centralWidget())
        self.setupLengthUnitManagement()
        self.centralWidget().addWidget(self.globalToolsW)
    def setupLengthUnitManagement(self):
        self.lengthUnitsW = LengthUnitItemView(self.globalToolsW,
                                               QApplication.instance().lengthUnitModel)
        self.globalToolsW.addItem(self.lengthUnitsW, self.tr("Length Units"))
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

    def onDatabaseConnected(self, msg):
        self.dbStatusW.setText(msg)
        self.centralWidget().setEnabled(True)
