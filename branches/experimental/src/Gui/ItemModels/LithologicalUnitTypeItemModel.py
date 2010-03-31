from DataManagementItemModel import DataManagementItemModel

from PyQt4.QtGui import *

from Model.LithologicalUnitType import LithologicalUnitType
from Gui.ItemModels.LithologicalUnitTypeItem import LithologicalUnitTypeItem
from Gui.Dialogs.LithologicalUnitTypeEditorDialog import LithologicalUnitTypeEditorDialog

class LithologicalUnitTypeItemModel(DataManagementItemModel):
    def __init__(self, parent):
        DataManagementItemModel.__init__(self, parent,
                                         LithologicalUnitType,
                                         LithologicalUnitTypeItem,
                                         LithologicalUnitTypeEditorDialog,
                                         LithologicalUnitType.name)
        self.headerStrings = [self.tr("Lithological Unit Types")]
