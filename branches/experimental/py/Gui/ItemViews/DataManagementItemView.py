from TreeView import TreeView

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from Model.Dataset import Dataset

class DataManagementItemView(TreeView):
    reloadRequest = pyqtSignal()
    editRequest = pyqtSignal(QModelIndex)
    exportToSvgRequest = pyqtSignal(Dataset)
    deleteRequest = pyqtSignal(QModelIndex)
    currentDatasetChanged = pyqtSignal(Dataset)

    def __init__(self, parent, model, askForConfirmationBeforeDeleting=True):
        TreeView.__init__(self, parent)
        self.askForConfirmationBeforeDeleting = askForConfirmationBeforeDeleting
        self.setModel(model)
        self.setContextMenuPolicy(Qt.CustomContextMenu)

        QApplication.instance().databaseConnected.connect(self.onDatabaseConnected)
        QApplication.instance().databaseClosed.connect(self.onDatabaseClosed)

        self.model().reloaded.connect(self.onReloaded)
        self.model().selectItemRequest.connect(self.onSelectItemRequest)

        self.reloadRequest.connect(self.model().reload)
        self.editRequest.connect(self.model().onEditRequest)
        self.deleteRequest.connect(self.model().onDeleteRequest)

        self.customContextMenuRequested.connect(self.onCustomContextMenuRequest)
        self.activated.connect(self.onIndexActivation)
        self.clicked.connect(self.onIndexActivation)
    def onReloaded(self):
        self.sortByColumn(0, Qt.AscendingOrder)
    def onDatabaseConnected(self):
        self.setEnabled(True)
        self.reloadRequest.emit()
    def onDatabaseClosed(self):
        self.setEnabled(False)
        if self.model() is not None:
            self.model().clear()
    def onCustomContextMenuRequest(self, pos):
        m = QMenu(self)
        createA = QAction(self.tr("Create..."), self)
        reloadA = QAction(self.tr("Reload"), self)
        editA = QAction(self.tr("Edit..."), self)
        exportSvgA = QAction(self.tr("Export to SVG..."), self)
        deleteA = QAction(self.tr("Delete"), self)

        createA.triggered.connect(self.model().onCreateNewRequest)
        reloadA.triggered.connect(self.onReloadRequest)
        editA.triggered.connect(self.onEditRequest)
        deleteA.triggered.connect(self.onDeleteRequest)
        exportSvgA.triggered.connect(self.onExportSvgRequest)

        m.addAction(createA)
        if len(self.selectedIndexes()) == 1:
            m.addAction(editA)
            m.addAction(exportSvgA)
        if len(self.selectedIndexes()) > 0:
            m.addAction(deleteA)
        m.insertSeparator(reloadA)
        m.addAction(reloadA)
        m.exec_(self.mapToGlobal(pos))
    def onExportSvgRequest(self):
        lst = self.selectedIndexes()
        if len(lst) != 1:
            return
        itm = self.model().itemFromIndex(lst[0])
        if itm is not None:
            self.exportToSvgRequest.emit(itm.data)
    def onReloadRequest(self):
        self.currentDatasetChanged.emit(None)
        self.reloadRequest.emit()
    def onEditRequest(self):
        lst = self.selectedIndexes()
        if len(lst) != 1:
            return
        self.editRequest.emit(lst[0])
    def onDeleteRequest(self):
        lst = self.selectedIndexes()
        if self.askForConfirmationBeforeDeleting:
            names = QStringList()

            for idx in lst:
                itm = self.model().itemFromIndex(idx)
                if itm is not None:
                    names.append(itm.data.name)

            if QMessageBox.Yes != QMessageBox.warning(self,
                                                      self.tr("Really Delete?"),
                                                      self.tr("Really delete this Datasets?\n%1")
                                                      .arg(names.join(", ")),
                                                      QMessageBox.Yes | QMessageBox.No):
                return
        for idx in lst:
            self.deleteRequest.emit(idx);
    def onSelectItemRequest(self, idx):
        if self.selectionModel() is None:
            self.setSelectionModel(QItemSelectionModel(self.model()))
        self.selectItemByIndex(idx)
    def selectItemByIndex(self, idx):
        if not idx.isValid():
            return
        self.selectionModel().select(idx, QItemSelectionModel.ClearAndSelect)
        self.selectionModel().setCurrentIndex(idx, QItemSelectionModel.ClearAndSelect)
        self.scrollTo(idx, QAbstractItemView.EnsureVisible)

    def onIndexActivation(self, idx):
        if not idx.isValid():
            self.currentDatasetChanged.emit(None)
            return
        itm = self.model().itemFromIndex(idx)
        if itm is None:
            self.currentDatasetChanged.emit(None)
        else:
            self.currentDatasetChanged.emit(itm.data)
    def selectDataset(self, dataset):
        if dataset is None:
            return
        idx = self.model().findIndexForDataset(dataset)
        if idx.isValid():
            self.selectItemByIndex(idx)
