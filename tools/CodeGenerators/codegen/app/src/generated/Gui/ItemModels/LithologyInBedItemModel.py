from InBedItemModel import *

from PyQt4.QtGui import *

from Model.LithologyInBed import LithologyInBed
from Gui.Dialogs.LithologyInBedEditorDialog import LithologyInBedEditorDialog

class LithologyInBedItem(StandardItem):
    def __init__(self, entity):
        StandardItem.__init__(self, entity)
        self.showData()

class LithologyInBedItemModel(InBedItemModel):
    def __init__(self, parent):
        InBedItemModel.__init__(self, parent,
                                LithologyInBed,
                                LithologyInBedItem,
                                LithologyInBedEditorDialog,
                                LithologyInBedFinder)
        self.headerStrings = [self.tr('Lithologies')]
