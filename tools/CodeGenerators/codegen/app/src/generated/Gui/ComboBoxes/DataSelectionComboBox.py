from ComboBox import *

from Logic.Model.Entity import *

class DataSelectionComboBox(ComboBox):
    currentEntityChanged = pyqtSignal(Entity)
    def __init__(self, parent, managementDialogClass, finderClass):
        ComboBox.__init__(self, parent)
        self.managementDialogClass = managementDialogClass
        self.finderClass = finderClass
        self.currentIndexChanged.connect(self.onIndexActivation)
        self.data = dict()
        self.setEnabled(False)
        QApplication.instance().databaseConnected.connect(self.onDatabaseConnected)
        QApplication.instance().databaseClosed.connect(self.onDatabaseDisconnected)
    def contextMenuEvent(self, e):
        e.accept()
        m = QMenu(self)
        reloadA = QAction(self.tr("Reload..."), self)
        reloadA.triggered.connect(self.onReload)
        manageA = QAction(self.tr("Manage..."), self)
        manageA.triggered.connect(self.onManage)
        m.addAction(reloadA)
        m.addAction(manageA)
        m.exec_(self.mapToGlobal(e.pos()))
    def onDatabaseConnected(self):
        self.onReload()
        self.setEnabled(True)
    def onDatabaseDisconnected(self):
        self.setEnabled(False)
    def onManage(self):
        dlg = self.managementDialogClass(self)
        dlg.exec_()
        self.onReload()
    def onReload(self):
        self.data = dict()
        self.clear()
        
        f = self.finderClass(self)
        self.insertItem(0, '')
        idx = 1
        data = f.findAll()
        for i in data:
            self.insertItem(idx, i.name)
            self.data[idx] = i
            idx += 1
        self.setEnabled(True)
    def onIndexActivation(self, idx):
        if idx == -1:
            self.currentEntityChanged.emit(None)
            return
        if idx not in self.data.keys():
            self.currentEntityChanged.emit(None)
            return
        self.currentEntityChanged.emit(self.data[idx])
    def selectEntity(self, ds):
        if ds is None:
            print self.__class__.__name__,": selection of None requested"
            return
        if ds not in self.data.values():
            print self.__class__.__name__,": entity ",ds," not in list"
            return
        for idx,entity in self.data.iteritems():
            if entity == ds:
                self.setCurrentIndex(idx)
                return
    def reload(self):
        self.onReload()
