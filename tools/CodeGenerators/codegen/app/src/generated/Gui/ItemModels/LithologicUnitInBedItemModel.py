from InBedItemModel import *

from PyQt4.QtGui import *

from Model.LithologicUnitInBed import LithologicUnitInBed
from Gui.Dialogs.LithologicUnitInBedEditorDialog import LithologicUnitInBedEditorDialog

class LithologicUnitInBedItem(StandardItem):
    def __init__(self, entity):
        StandardItem.__init__(self, entity)
        self.showData()

class LithologicUnitInBedItemModel(InBedItemModel):
    def __init__(self, parent):
        InBedItemModel.__init__(self, parent,
                                LithologicUnitInBed,
                                LithologicUnitInBedItem,
                                LithologicUnitInBedEditorDialog,
                                LithologicUnitInBedFinder)
        self.headerStrings = [self.tr('Lithologic Units')]
