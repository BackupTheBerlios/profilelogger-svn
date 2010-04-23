from ManagementItemModel import *

from PyQt4.QtGui import *
from PyQt4.QtCore import *

class InBedManagementItemModel(ManagementItemModel):
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
        self.bed = None
    def onBedChange(self, bed):
        self.bed = bed
        self.clear();
        self.disableViews.emit()
        if self.bed is not None:
            self.reload()
    def setBed(self, bed):
        self.onBedChange(bed)
    def hasBed(self):
        return self.bed is not None
    def reload(self):
        self.disableViews.emit()
        self.clear()
        if not self.hasBed():
            return
        self.setHorizontalHeaderLabels(self.headerStrings)
        self.data = self.getSession().query(self.dataClass).order_by(self.orderColumn).filter(self.dataClass.bed==self.bed).all()
        for u in self.data:
            self.appendItem(u)
        self.reloaded.emit()
        self.enableViews.emit()
    def onCreateNewRequest(self):
        dlg = self.editorDialogClass(QApplication.activeWindow(), self.dataClass(bed=self.bed))
        if QDialog.Accepted == dlg.exec_():
            self.reload()
