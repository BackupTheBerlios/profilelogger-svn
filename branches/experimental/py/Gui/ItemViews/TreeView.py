from PyQt4.QtGui import *
from PyQt4.QtCore import *

class TreeView(QTreeView):
    reloadRequest = pyqtSignal()
    editRequest = pyqtSignal(QModelIndex)
    deleteRequest = pyqtSignal(QModelIndex)

    def __init__(self, parent):
        QTreeView.__init__(self, parent)
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setSortingEnabled(True)
        QApplication.instance().databaseConnected.connect(self.onDatabaseConnected)
        QApplication.instance().databaseClosed.connect(self.onDatabaseClosed)
    def onReloaded(self):
        self.sortByColumn(0, Qt.AscendingOrder)
    def onDatabaseConnected(self):
        self.setEnabled(True)
        self.reloadRequest.emit()
    def onDatabaseClosed(self):
        self.setEnabled(False)
        if self.model() is not None:
            self.model().clear()
