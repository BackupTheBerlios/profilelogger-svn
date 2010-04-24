from InBedItemModel import *

from PyQt4.QtGui import *

from Model.FossilInBed import FossilInBed
from Gui.Dialogs.FossilInBedEditorDialog import FossilInBedEditorDialog

class FossilInBedItem(StandardItem):
    def __init__(self, entity):
        StandardItem.__init__(self, entity)
        self.showData()

class FossilInBedItemModel(InBedItemModel):
    def __init__(self, parent):
        InBedItemModel.__init__(self, parent,
                                FossilInBed,
                                FossilInBedItem,
                                FossilInBedEditorDialog,
                                FossilInBedFinder)
        self.headerStrings = [self.tr('Fossils')]
