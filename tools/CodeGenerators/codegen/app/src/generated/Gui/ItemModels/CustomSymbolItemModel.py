from InProjectItemModel import *

from PyQt4.QtGui import *

from Model.CustomSymbol import CustomSymbol
from Gui.Dialogs.CustomSymbolEditorDialog import CustomSymbolEditorDialog

class CustomSymbolItem(StandardItem):
    def __init__(self, entity):
        StandardItem.__init__(self, entity)
        self.showData()

class CustomSymbolItemModel(InProjectItemModel):
    def __init__(self, parent):
        InProjectItemModel.__init__(self, parent,
                                    CustomSymbol,
                                    CustomSymbolItem,
                                    CustomSymbolEditorDialog,
                                    CustomSymbolFinder)
        self.headerStrings = [self.tr('Custom Symbols')]
