from InProjectItemModel import *

from PyQt4.QtGui import *

from Model.LithologicUnitType import LithologicUnitType
from Gui.Dialogs.LithologicUnitTypeEditorDialog import LithologicUnitTypeEditorDialog

class LithologicUnitTypeItem(StandardItem):
    def __init__(self, entity):
        StandardItem.__init__(self, entity)
        self.showData()

class LithologicUnitTypeItemModel(InProjectItemModel):
    def __init__(self, parent):
        InProjectItemModel.__init__(self, parent,
                                    LithologicUnitType,
                                    LithologicUnitTypeItem,
                                    LithologicUnitTypeEditorDialog,
                                    LithologicUnitTypeFinder)
        self.headerStrings = [self.tr('Lithological Unit Types')]
