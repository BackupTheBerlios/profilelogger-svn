from DataManagementItemModel import DataManagementItemModel

from PyQt4.QtGui import *
from PyQt4.QtCore import *

class DataInProfileManagementItemModel(DataManagementItemModel):
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
        self.profile = None
    def onProfileChange(self, profile):
        self.profile = profile
        self.clear();
        self.disableViews.emit()
        if self.profile is not None:
            self.reload()
    def hasProfile(self):
        return self.profile is not None
    def reload(self):
        self.disableViews.emit()
        self.clear()
        if not self.hasProfile():
            return
        self.setHorizontalHeaderLabels(self.headerStrings)
        self.data = self.getSession().query(self.dataClass).order_by(self.orderColumn).filter(self.dataClass.profile==self.profile).all()
        for u in self.data:
            self.appendItem(u)
        self.reloaded.emit()
        self.enableViews.emit()
    def onCreateNewRequest(self):
        dlg = self.editorDialogClass(QApplication.activeWindow(), self.dataClass(profile=self.profile))
        if QDialog.Accepted == dlg.exec_():
            self.reload()
