from StandardItemModel import StandardItemModel

from PyQt4.QtGui import *
from PyQt4.QtCore import *

class DataSelectionItemModel(StandardItemModel):
    reloaded = pyqtSignal()
    selectItemRequest = pyqtSignal(QModelIndex)

    def __init__(self, parent,
                 dataClass=None,
                 itemClass=None,
                 orderColumn=None,
                 headerStrings=None):
        StandardItemModel.__init__(self, parent)
        QApplication.instance().databaseConnected.connect(self.onDatabaseConnected)
        QApplication.instance().databaseClosed.connect(self.onDatabaseClosed)
        self.dataClass = dataClass
        self.itemClass = itemClass
        self.headerStrings = headerStrings
        self.orderColumn = orderColumn
        self.data = []
        self.intKeyData = dict()
    def getSession(self):
        return QApplication.instance().db.session
    def onDatabaseConnected(self):
        self.reload()
    def onDatabaseClosed(self):
        self.clear()
    def getDataFromIntIndex(self, intIdx):
        return self.intKeyData[intIdx]
    def getIntIndexFromData(self, data):
        for k,v in self.intKeyData.iteritems():
            if data == v:
                return k
        return -1
    def getDataFromIndex(self, idx):
        itm = self.itemFromIndex(idx)
        if itm is None:
            return None
        return itm.data
    def findItemForId(self, id):
        r = 0
        while r < self.rowCount():
            ret = self.item(r)
            if ret.data.id == id:
                return ret;
            r += 1;
        return None
    def findIndexForDataset(self, dataset):
        if dataset is None:
            return QModelIndex()
        itm = self.findItemForId(dataset.id)
        if itm is None:
            return QModelIndex()
        return self.indexFromItem(itm)
    def appendItem(self, dataset):
        self.insertRow(self.lastIntIndex, self.itemClass(dataset))
        self.intKeyData[self.lastIntIndex] = dataset
        print "idx: %i, value: %s" % (self.lastIntIndex, dataset)
    def reload(self):
        self.intKeyData = dict()
        self.lastIntIndex = 0
        self.clear()
        self.setHorizontalHeaderLabels(self.headerStrings)
        self.data = self.getSession().query(self.dataClass).order_by(self.orderColumn).all()
        for u in self.data:
            self.appendItem(u)
            self.lastIntIndex += 1
        self.reloaded.emit()
