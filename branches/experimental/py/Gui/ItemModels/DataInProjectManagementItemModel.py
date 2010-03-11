from DataManagementItemModel import DataManagementItemModel

from PyQt4.QtGui import *
from PyQt4.QtCore import *

class DataInProjectManagementItemModel(DataManagementItemModel):
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
        self.project = None
    def onProjectChange(self, project):
        self.project = project
        self.clear();
        self.disableViews.emit()
        if self.project is not None:
            self.reload()
    def hasProject(self):
        return self.project is not None
    def reload(self):
        self.disableViews.emit()
        self.clear()
        if not self.hasProject():
            return
        self.setHorizontalHeaderLabels(self.headerStrings)
        self.data = self.getSession().query(self.dataClass).order_by(self.orderColumn).filter(self.dataClass.project==self.project).all()
        for u in self.data:
            self.appendItem(u)
        self.reloaded.emit()
        self.enableViews.emit()
    def onCreateNewRequest(self):
        dlg = self.editorDialogClass(QApplication.activeWindow(), self.dataClass(project=self.project))
        if QDialog.Accepted == dlg.exec_():
            self.reload()
