from InProjectItemModel import *

from PyQt4.QtGui import *

from Model.LithologicUnit import LithologicUnit
from Gui.Dialogs.LithologicUnitEditorDialog import LithologicUnitEditorDialog

class LithologicUnitItem(StandardItem):
    def __init__(self, entity):
        StandardItem.__init__(self, entity)
        self.showData()

class LithologicUnitItemModel(InProjectItemModel):
    def __init__(self, parent):
        InProjectItemModel.__init__(self, parent,
                                    LithologicUnit,
                                    LithologicUnitItem,
                                    LithologicUnitEditorDialog,
                                    LithologicUnitFinder)
        self.headerStrings = [self.tr('Lithological Units')]
