from PyQt4.QtGui import *
from PyQt4.QtCore import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
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
