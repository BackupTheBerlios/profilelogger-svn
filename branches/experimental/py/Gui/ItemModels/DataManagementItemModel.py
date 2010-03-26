from StandardItemModel import StandardItemModel

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from Gui.Dialogs.DatabaseExceptionDialog import DatabaseExceptionDialog

from sqlalchemy.exc import *
from sqlalchemy.orm.exc import *

class DataManagementItemModel(StandardItemModel):
    reloaded = pyqtSignal()
    selectItemRequest = pyqtSignal(QModelIndex)

    def __init__(self, parent,
                 dataClass=None,
                 itemClass=None,
                 editorDialogClass=None,
                 orderColumn=None,
                 headerStrings=None):
        StandardItemModel.__init__(self, parent)
        QApplication.instance().databaseConnected.connect(self.onDatabaseConnected)
        QApplication.instance().databaseClosed.connect(self.onDatabaseClosed)
        self.editorDialogClass = editorDialogClass
        self.dataClass = dataClass
        self.itemClass = itemClass
        self.headerStrings = headerStrings
        self.orderColumn = orderColumn
        self.data = []
    def getSession(self):
        return QApplication.instance().db.session
    def onDatabaseConnected(self):
        self.reload()
    def onDatabaseClosed(self):
        self.clear()
    def onCreateNewRequest(self):
        dlg = self.editorDialogClass(QApplication.activeWindow(), self.dataClass())
        if QDialog.Accepted == dlg.exec_():
            self.reload()
    def getDataFromIndex(self, idx):
        itm = self.itemFromIndex(idx)
        if itm is None:
            return None
        return itm.data
    def onEditRequest(self, idx):
        data = self.getDataFromIndex(idx)
        if data is None:
            return
        dlg = self.editorDialogClass(QApplication.activeWindow(), data)
        if QDialog.Accepted == dlg.exec_():
            self.reload()
    def onDeleteRequest(self, idx):
        itm = self.itemFromIndex(idx)
        data = itm.data
        try:
            self.getSession().delete(data)
            self.getSession().commit();
            self.reload()
        except IntegrityError, e:
            dlg = DatabaseExceptionDialog(QApplication.activeWindow(), e)
            dlg.exec_()
            QApplication.instance().db.session.rollback()
        except ConcurrentModificationError, e:
            dlg = DatabaseExceptionDialog(QApplication.activeWindow(), e)
            dlg.exec_()
            QApplication.instance().db.session.rollback()
        except ProgrammingError, e:
            dlg = DatabaseExceptionDialog(QApplication.activeWindow(), e)
            dlg.exec_()
            QApplication.instance().db.session.rollback()
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
        self.appendRow(self.itemClass(dataset))
    def reload(self):
        self.clear()
        self.setHorizontalHeaderLabels(self.headerStrings)
        self.data = self.getSession().query(self.dataClass).order_by(self.orderColumn).all()
        for u in self.data:
            self.appendItem(u)
        self.reloaded.emit()
