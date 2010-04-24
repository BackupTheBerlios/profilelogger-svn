from ManagementItemModel import ManagementItemModel

from PyQt4.QtGui import *

from Logic.Model.LengthUnit import LengthUnit
from Gui.Dialogs.LengthUnitEditorDialog import LengthUnitEditorDialog
from ManagmentItemModel import *

class LengthUnitItem(StandardItem):
    def __init__(self, entity):
        StandardItem.__init__(self, entity)
        self.showData()

class LengthUnitItemModel(ManagementItemModel):
    def __init__(self, parent):
        ManagementItemModel.__init__(self, parent,
                                     LengthUnit,
                                     LengthUnitItem,
                                     LengthUnitEditorDialog,
                                     LengthUnitFinder)
        self.headerStrings = [self.tr('Length Units')]
