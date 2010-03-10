from StandardItemModel import StandardItemModel

from PyQt4.QtGui import *

from Model.LengthUnit import LengthUnit
from Gui.ItemModels.LengthUnitItem import LengthUnitItem
from Gui.Dialogs.LengthUnitEditorDialog import LengthUnitEditorDialog

class LengthUnitItemModel(StandardItemModel):
    def __init__(self, parent):
        StandardItemModel.__init__(self, parent,
                                   LengthUnit,
                                   LengthUnitItem,
                                   LengthUnitEditorDialog,
                                   LengthUnit.milliMetre)
        self.headerStrings = [self.tr("Length Units")]
