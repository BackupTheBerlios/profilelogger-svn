from ComboBox import *

from Model.Entity import *

class InProfileSelectionComboBox(QComboBox):
    currentEntityChanged = pyqtSignal(Entity)
    def __init__(self, parent, managementDialogClass, finderClass):
        QComboBox.__init__(self, parent)
        self.managementDialogClass = managementDialogClass
        self.finderClass = finderClass
        self.currentIndexChanged.connect(self.onIndexActivation)
        self.data = dict()
        self.profile = None
        self.setEnabled(self.hasProfile())
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
        dlg = self.managementDialogClass(self, self.profile)
        dlg.exec_()
        self.onReload()
    def reload(self):
        self.data = dict()
        self.clear()
        
        if not self.hasProfile():
            return
        
        f = self.finderClass(self)
        self.insertItem(0, '')
        idx = 1
        for i in f.findAll(self.profile):
            self.insertItem(idx, i.name)
            self.data[idx] = i
            idx += 1
    def onReload(self):
        self.reload()
    def onIndexActivation(self, idx):
        if idx == -1:
            self.currentEntityChanged.emit(None)
            return
        if idx not in self.data.keys():
            self.currentEntityChanged.emit(None)
            return
        self.currentEntityChanged.emit(self.data[idx])
    def onProfileChange(self, p):
        self.profile = p
        self.reload()
        self.setEnabled(self.hasProfile())
    def hasProfile(self):
        return self.profile is not None
    def setProfile(self, p):
        self.onProfileChange(p)
