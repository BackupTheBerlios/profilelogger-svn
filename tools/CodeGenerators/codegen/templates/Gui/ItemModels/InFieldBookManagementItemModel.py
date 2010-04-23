from ManagementItemModel import *

from PyQt4.QtGui import *
from PyQt4.QtCore import *

class InFieldBookManagementItemModel(ManagementItemModel):
    enableViews = pyqtSignal()
    disableViews = pyqtSignal()
    reloaded = pyqtSignal()
    selectItemRequest = pyqtSignal(QModelIndex)

    def __init__(self, parent,
                 dataClass=None,
                 itemClass=None,
                 editorDialogClass=None,
                 orderColumn=None,
                 headerStrings=None):
        ManagementItemModel.__init__(self, parent, 
                                     dataClass, itemClass,
                                     editorDialogClass,
                                     orderColumn,
                                     headerStrings)
        self.fieldBook = None
    def onFieldBookChange(self, fieldBook):
        self.fieldBook = fieldBook
        self.clear();
        self.disableViews.emit()
        if self.fieldBook is not None:
            self.reload()
    def setFieldBook(self, fieldBook):
        self.onFieldBookChange(fieldBook)
    def hasFieldBook(self):
        return self.fieldBook is not None
    def reload(self):
        self.disableViews.emit()
        self.clear()
        if not self.hasFieldBook():
            return
        self.setHorizontalHeaderLabels(self.headerStrings)
        self.data = self.getSession().query(self.dataClass).order_by(self.orderColumn).filter(self.dataClass.fieldBook==self.fieldBook).all()
        for u in self.data:
            self.appendItem(u)
        self.reloaded.emit()
        self.enableViews.emit()
    def onCreateNewRequest(self):
        dlg = self.editorDialogClass(QApplication.activeWindow(), self.dataClass(fieldBook=self.fieldBook))
        if QDialog.Accepted == dlg.exec_():
            self.reload()
