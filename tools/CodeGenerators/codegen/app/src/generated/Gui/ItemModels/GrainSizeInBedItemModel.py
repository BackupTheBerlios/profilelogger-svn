from InBedItemModel import *

from PyQt4.QtGui import *

from Model.GrainSizeInBed import GrainSizeInBed
from Gui.Dialogs.GrainSizeInBedEditorDialog import GrainSizeInBedEditorDialog

class GrainSizeInBedItem(StandardItem):
    def __init__(self, entity):
        StandardItem.__init__(self, entity)
        self.showData()

class GrainSizeInBedItemModel(InBedItemModel):
    def __init__(self, parent):
        InBedItemModel.__init__(self, parent,
                                GrainSizeInBed,
                                GrainSizeInBedItem,
                                GrainSizeInBedEditorDialog,
                                GrainSizeInBedFinder)
        self.headerStrings = [self.tr('Grain Sizes')]
