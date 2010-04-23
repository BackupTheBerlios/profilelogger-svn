from ManagementItemModel import *

from PyQt4.QtGui import *
from PyQt4.QtCore import *

class InProjectManagementItemModel(ManagementItemModel):
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
        self.project = None
    def onProjectChange(self, project):
        self.project = project
        self.clear();
        self.disableViews.emit()
        if self.project is not None:
            self.reload()
    def setProject(self, project):
        self.onProjectChange(project)
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
