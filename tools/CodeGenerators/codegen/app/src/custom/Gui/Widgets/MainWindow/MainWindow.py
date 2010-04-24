from PyQt4.QtCore import *
from PyQt4.QtGui import *

from Action import *
from Menu import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.actions = {}
        self.menues = {}
        self.setupStatusBar()
        self.setupActions()
        self.setupMenuBar()
        self.setupToolBar()
    def setupStatusBar(self):
        pass
    def setupActions(self):
        self.actions['quit'] = Action(self.tr('&Quit'), self, QApplication.instance().quit, QKeySequence('Ctrl+o'))
        self.actions['open database'] = Action(self.tr('&Connect To Database...'), self, QApplication.instance().connectToDatabase)
        self.actions['close database'] = Action(self.tr('&Disconnect From Database...'), self, QApplication.instance().connectToDatabase)

    def setupMenuBar(self):
        self.menues['file'] = Menu(self.tr('&File'), self, self.getFileActions())
        self.menues['database'] = Menu(self.tr('&Database'), self, self.getDatabaseActions())
        self.menuBar().addMenu(self.menues['file'])
        self.menuBar().addMenu(self.menues['database'])
    def getFileActions(self):
        return [(self.actions['quit']),]
    def getDatabaseActions(self):
        return [self.actions['open database'],
                self.actions['close database'],]
    def setupToolBar(self):
        pass
