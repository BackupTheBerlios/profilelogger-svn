from DataManagementItemModel import DataManagementItemModel

from PyQt4.QtGui import *
from PyQt4.QtCore import *

class DataInProfileAssemblyManagementItemModel(DataManagementItemModel):
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
        DataManagementItemModel.__init__(self, parent, 
                                         dataClass, itemClass,
                                         editorDialogClass,
                                         orderColumn,
                                         headerStrings)
        self.profileAssembly = None
    def onProfileAssemblyChange(self, profileAssembly):
        self.profileAssembly = profileAssembly
        self.clear();
        self.disableViews.emit()
        if self.profileAssembly is not None:
            self.reload()
    def setProfileAssembly(self, profileAssembly):
        self.onProfileAssemblyChange(profileAssembly)
    def hasProfileAssembly(self):
        return self.profileAssembly is not None
    def reload(self):
        self.disableViews.emit()
        self.clear()
        if not self.hasProfileAssembly():
            return
        self.setHorizontalHeaderLabels(self.headerStrings)
        self.data = self.getSession().query(self.dataClass).order_by(self.orderColumn).filter(self.dataClass.profileAssembly==self.profileAssembly).all()
        for u in self.data:
            self.appendItem(u)
        self.reloaded.emit()
        self.enableViews.emit()
    def onCreateNewRequest(self):
        dlg = self.editorDialogClass(QApplication.activeWindow(), self.dataClass(profileAssembly=self.profileAssembly))
        if QDialog.Accepted == dlg.exec_():
            self.reload()
