from DataInProjectManagementItemModel import DataInProjectManagementItemModel

from PyQt4.QtGui import *

from Model.CustomSymbol import CustomSymbol
from Gui.ItemModels.CustomSymbolItem import CustomSymbolItem
from Gui.Dialogs.CustomSymbolEditorDialog import CustomSymbolEditorDialog

class CustomSymbolItemModel(DataInProjectManagementItemModel):
    def __init__(self, parent):
        DataInProjectManagementItemModel.__init__(self, parent,
                                                  CustomSymbol,
                                                  CustomSymbolItem,
                                                  CustomSymbolEditorDialog,
                                                  CustomSymbol.name)
        self.headerStrings = [self.tr("Custom Symbols")]
