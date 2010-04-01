from ComboBox import *

from Model.Dataset import *

class DataInProjectSelectionComboBox(ComboBox):
    currentDatasetChanged = pyqtSignal(Dataset)
    def __init__(self, parent, managementDialogClass, finderClass):
        ComboBox.__init__(self, parent)
        self.managementDialogClass = managementDialogClass
        self.finderClass = finderClass
        self.currentIndexChanged.connect(self.onIndexActivation)
        self.data = dict()
        self.project = None
        self.setEnabled(self.hasProject())
    def contextMenuEvent(self, e):
        m = QMenu(self)
        reloadA = QAction(self.tr("Reload..."), self)
        reloadA.triggered.connect(self.onReload)
        manageA = QAction(self.tr("Manage..."), self)
        manageA.triggered.connect(self.onManage)
        m.addAction(reloadA)
        m.addAction(manageA)
        m.exec_(self.mapToGlobal(e.pos()))
    def onManage(self):
        dlg = self.managementDialogClass(self, self.project)
        dlg.exec_()
        self.onReload()
    def reload(self):
        self.data = dict()
        self.clear()
        
        if not self.hasProject():
            return
        
        f = self.finderClass(self)
        self.insertItem(0, '')
        idx = 1
        for i in f.findAll(self.project):
            self.insertItem(idx, i.name)
            self.data[idx] = i
            idx += 1
    def onReload(self):
        self.reload()
    def onIndexActivation(self, idx):
        if idx == -1:
            self.currentDatasetChanged.emit(None)
            return
        if idx not in self.data.keys():
            self.currentDatasetChanged.emit(None)
            return
        self.currentDatasetChanged.emit(self.data[idx])
    def onProjectChange(self, p):
        self.project = p
        self.reload()
        self.setEnabled(self.hasProject())
    def hasProject(self):
        return self.project is not None
    def setProject(self, p):
        self.onProjectChange(p)
