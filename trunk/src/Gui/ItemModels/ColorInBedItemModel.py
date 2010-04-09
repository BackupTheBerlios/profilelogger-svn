from DataInBedManagementItemModel import DataInBedManagementItemModel

from PyQt4.QtGui import *

from Model.ColorInBed import ColorInBed
from Gui.ItemModels.ColorInBedItem import ColorInBedItem
from Gui.Dialogs.ColorInBedEditorDialog import ColorInBedEditorDialog

class ColorInBedItemModel(DataInBedManagementItemModel):
    def __init__(self, parent):
        DataInBedManagementItemModel.__init__(self, parent,
                                              ColorInBed,
                                              ColorInBedItem,
                                              ColorInBedEditorDialog,
                                              ColorInBed.id)
        self.headerStrings = [self.tr("Colors")]
