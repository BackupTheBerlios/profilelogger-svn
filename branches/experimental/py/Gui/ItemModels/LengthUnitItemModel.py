from StandardItemModel import StandardItemModel

from PyQt4.QtGui import *

from Model.LengthUnit import LengthUnit
from Gui.ItemModels.LengthUnitItem import LengthUnitItem
from Gui.Dialogs.LengthUnitEditorDialog import LengthUnitEditorDialog

class LengthUnitItemModel(StandardItemModel):
    def __init__(self, parent):
        StandardItemModel.__init__(self, parent)
    def onCreateNewRequest(self):
        tmp = LengthUnit()
        dlg = LengthUnitEditorDialog(QApplication.activeWindow(), tmp)
        if QDialog.Accepted == dlg.exec_():
            s = self.getSession()
            s.add(tmp)
            s.commit()
            self.reload()

    def onEditRequest(self, idx):
        tmp = self.itemFromIndex(idx)
        if tmp is None:
            return
        data = tmp.data
        if data is None:
            return
        dlg = LengthUnitEditorDialog(QApplication.activeWindow(), data)
        s = self.getSession()
        if QDialog.Accepted == dlg.exec_():
            s.flush()
            s.commit()
            self.reload()
        else:
            s.refresh(data)
    def onDeleteRequest(self, idx):
        itm = self.itemFromIndex(idx)
        data = itm.data
        self.getSession().delete(data)
        self.getSession().commit();
        self.reload()
    def reload(self):
        self.clear()
        self.setHorizontalHeaderLabels([self.tr("Length Units")])
        self.data = self.getSession().query(LengthUnit).order_by(LengthUnit.milliMetre).all()
        for u in self.data:
            self.appendItem(u)
        self.reloaded.emit()

    def findItemForLengthUnit(self, id):
        r = 0
        while r < self.rowCount():
            ret = self.item(r)
            if ret.data.id == id:
                return ret;
            r += 1;
        return None
    def findIndexForLengthUnit(self, dataset):
        if dataset is None:
            return QModelIndex()
        itm = self.findItemForLengthUnit(dataset.id)
        if itm is None:
            return QModelIndex()
        return self.indexFromItem(itm)

    def appendItem(self, dataset):
        self.appendRow(LengthUnitItem(dataset))
