from DataInBedManagementItemModel import DataInBedManagementItemModel

from PyQt4.QtGui import *

from Model.CustomSymbolInBed import CustomSymbolInBed
from Gui.ItemModels.CustomSymbolInBedItem import CustomSymbolInBedItem
from Gui.Dialogs.CustomSymbolInBedEditorDialog import CustomSymbolInBedEditorDialog

class CustomSymbolInBedItemModel(DataInBedManagementItemModel):
    def __init__(self, parent):
        DataInBedManagementItemModel.__init__(self, parent,
                                              CustomSymbolInBed,
                                              CustomSymbolInBedItem,
                                              CustomSymbolInBedEditorDialog,
                                              CustomSymbolInBed.id)
        self.headerStrings = [self.tr("Custom Symbols")]
