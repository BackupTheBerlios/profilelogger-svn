from PyQt4.QtGui import *
from PyQt4.QtCore import *

class StandardItemModel(QStandardItemModel):
    reloaded = pyqtSignal()
    selectItemRequest = pyqtSignal(QModelIndex)

    def __init__(self, parent):
        QStandardItemModel.__init__(self, parent)
    def getSession(self):
        return QApplication.instance().db.session
