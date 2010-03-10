from Gui.ItemViews.TreeView import TreeView

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from Model.LengthUnit import LengthUnit

class LengthUnitItemView(TreeView):
    reloadRequest = pyqtSignal()
    editRequest = pyqtSignal(QModelIndex)
    deleteRequest = pyqtSignal(QModelIndex)
    currentLengthUnitChanged = pyqtSignal(LengthUnit)

    def __init__(self, parent, model):
        TreeView.__init__(self, parent)
        self.setModel(model)
        self.setContextMenuPolicy(Qt.CustomContextMenu)

        self.model().reloaded.connect(self.onReloaded)
        self.model().selectItemRequest.connect(self.onSelectItemRequest)

        self.reloadRequest.connect(self.model().reload)
        self.editRequest.connect(self.model().onEditRequest)
        self.deleteRequest.connect(self.model().onDeleteRequest)

        self.customContextMenuRequested.connect(self.onCustomContextMenuRequest)
        self.activated.connect(self.onIndexActivation)
        self.clicked.connect(self.onIndexActivation)

    def onCustomContextMenuRequest(self, pos):
        m = QMenu(self)
        createA = QAction(self.tr("Create..."), self)
        reloadA = QAction(self.tr("Reload"), self)
        editA = QAction(self.tr("Edit..."), self)
        deleteA = QAction(self.tr("Delete"), self)

        createA.triggered.connect(self.model().onCreateNewRequest)
        reloadA.triggered.connect(self.onReloadRequest)
        editA.triggered.connect(self.onEditRequest)
        deleteA.triggered.connect(self.onDeleteRequest)

        m.addAction(createA)
        if len(self.selectedIndexes()) == 1:
            m.addAction(editA)
        if len(self.selectedIndexes()) > 0:
            m.addAction(deleteA)
        m.insertSeparator(reloadA)
        m.addAction(reloadA)
        m.exec_(self.mapToGlobal(pos))

    def onReloadRequest(self):
        self.currentLengthUnitChanged.emit(None)
        self.reloadRequest.emit()
    def onEditRequest(self):
        lst = self.selectedIndexes()
        if len(lst) != 1:
            return
        self.editRequest.emit(lst[0])
    def onDeleteRequest(self):
        lst = self.selectedIndexes()
        names = QStringList()

        for idx in lst:
            itm = self.model().itemFromIndex(idx)
            if itm is not None:
                names.append(itm.data.name)

        if QMessageBox.Yes == QMessageBox.warning(self,
                                                  self.tr("Really Delete?"),
                                                  self.tr("Really delete this Datasets?\n%1")
                                                  .arg(names.join(", ")),
                                                  QMessageBox.Yes | QMessageBox.No):
            for idx in lst:
                self.deleteRequest.emit(idx);

    def onSelectItemRequest(self, idx):
        if self.selectionModel() is None:
            self.setSelectionModel(QItemSelectionModel(self.model()))
        self.selectionModel().select(idx, QItemSelectionModel.ClearAndSelect)
        self.selectionModel().setCurrentIndex(idx, QItemSelectionModel.ClearAndSelect)
        self.scrollTo(idx, QAbstractItemView.EnsureVisible)

    def onIndexActivation(self, idx):
        if not idx.isValid():
            self.currentLengthUnitChanged.emit(None)
            return
        itm = self.model().itemFromIndex(idx)
        if itm is None:
            self.currentLengthUnitChanged.emit(None)
        else:
            self.currentLengthUnitChanged.emit(itm)
