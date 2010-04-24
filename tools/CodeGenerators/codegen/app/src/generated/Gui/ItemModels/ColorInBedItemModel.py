from InBedItemModel import *

from PyQt4.QtGui import *

from Model.ColorInBed import ColorInBed
from Gui.Dialogs.ColorInBedEditorDialog import ColorInBedEditorDialog

class ColorInBedItem(StandardItem):
    def __init__(self, entity):
        StandardItem.__init__(self, entity)
        self.showData()

class ColorInBedItemModel(InBedItemModel):
    def __init__(self, parent):
        InBedItemModel.__init__(self, parent,
                                ColorInBed,
                                ColorInBedItem,
                                ColorInBedEditorDialog,
                                ColorInBedFinder)
        self.headerStrings = [self.tr('Colors')]
