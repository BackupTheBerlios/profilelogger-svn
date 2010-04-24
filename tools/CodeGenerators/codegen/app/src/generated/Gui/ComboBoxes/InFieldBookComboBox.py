from ComboBox import *

from Model.Entity import *

class InFieldBookSelectionComboBox(QComboBox):
    currentEntityChanged = pyqtSignal(Entity)
    def __init__(self, parent, managementDialogClass, finderClass):
        QComboBox.__init__(self, parent)
        self.managementDialogClass = managementDialogClass
        self.finderClass = finderClass
        self.currentIndexChanged.connect(self.onIndexActivation)
        self.data = dict()
        self.fieldBook = None
        self.setEnabled(self.hasFieldBook())
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
        dlg = self.managementDialogClass(self, self.fieldBook)
        dlg.exec_()
        self.onReload()
    def reload(self):
        self.data = dict()
        self.clear()
        
        if not self.hasFieldBook():
            return
        
        f = self.finderClass(self)
        self.insertItem(0, '')
        idx = 1
        for i in f.findAll(self.fieldBook):
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
    def onFieldBookChange(self, p):
        self.fieldBook = p
        self.reload()
        self.setEnabled(self.hasFieldBook())
    def hasFieldBook(self):
        return self.fieldBook is not None
    def setFieldBook(self, p):
        self.onFieldBookChange(p)
