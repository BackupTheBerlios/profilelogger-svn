from DataManagementItemModel import DataManagementItemModel

from PyQt4.QtGui import *

from Model.LengthUnit import LengthUnit
from Gui.ItemModels.LengthUnitItem import LengthUnitItem
from Gui.Dialogs.LengthUnitEditorDialog import LengthUnitEditorDialog

class LengthUnitItemModel(DataManagementItemModel):
    def __init__(self, parent):
        DataManagementItemModel.__init__(self, parent,
                                         LengthUnit,
                                         LengthUnitItem,
                                         LengthUnitEditorDialog,
                                         LengthUnit.microMetre)
        self.headerStrings = [self.tr("Length Units")]
