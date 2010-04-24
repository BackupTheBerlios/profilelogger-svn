from InBedItemModel import *

from PyQt4.QtGui import *

from Model.CustomSymbolInBed import CustomSymbolInBed
from Gui.Dialogs.CustomSymbolInBedEditorDialog import CustomSymbolInBedEditorDialog

class CustomSymbolInBedItem(StandardItem):
    def __init__(self, entity):
        StandardItem.__init__(self, entity)
        self.showData()

class CustomSymbolInBedItemModel(InBedItemModel):
    def __init__(self, parent):
        InBedItemModel.__init__(self, parent,
                                CustomSymbolInBed,
                                CustomSymbolInBedItem,
                                CustomSymbolInBedEditorDialog,
                                CustomSymbolInBedFinder)
        self.headerStrings = [self.tr('Custom Symbols')]
