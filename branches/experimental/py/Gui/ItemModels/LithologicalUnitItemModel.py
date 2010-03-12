from DataManagementItemModel import DataManagementItemModel

from PyQt4.QtGui import *

from Model.LithologicalUnit import LithologicalUnit
from Gui.ItemModels.LithologicalUnitItem import LithologicalUnitItem
from Gui.Dialogs.LithologicalUnitEditorDialog import LithologicalUnitEditorDialog

class LithologicalUnitItemModel(DataManagementItemModel):
    def __init__(self, parent):
        DataManagementItemModel.__init__(self, parent,
                                         LithologicalUnit,
                                         LithologicalUnitItem,
                                         LithologicalUnitEditorDialog,
                                         LithologicalUnit.name)
        self.headerStrings = [self.tr("Lithological Units")]
