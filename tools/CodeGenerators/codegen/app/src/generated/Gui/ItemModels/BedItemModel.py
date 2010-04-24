from InProfileItemModel import *

from PyQt4.QtGui import *

from Model.Bed import Bed
from Gui.Dialogs.BedEditorDialog import BedEditorDialog

class BedItem(StandardItem):
    def __init__(self, entity):
        StandardItem.__init__(self, entity)
        self.showData()

class BedItemModel(InProfileItemModel):
    def __init__(self, parent):
        InProfileItemModel.__init__(self, parent,
                                    Bed,
                                    BedItem,
                                    BedEditorDialog,
                                    BedFinder)
        self.headerStrings = [self.tr('Beds')]
