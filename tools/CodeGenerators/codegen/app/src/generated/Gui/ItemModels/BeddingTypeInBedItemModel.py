from InBedItemModel import *

from PyQt4.QtGui import *

from Model.BeddingTypeInBed import BeddingTypeInBed
from Gui.Dialogs.BeddingTypeInBedEditorDialog import BeddingTypeInBedEditorDialog

class BeddingTypeInBedItem(StandardItem):
    def __init__(self, entity):
        StandardItem.__init__(self, entity)
        self.showData()

class BeddingTypeInBedItemModel(InBedItemModel):
    def __init__(self, parent):
        InBedItemModel.__init__(self, parent,
                                BeddingTypeInBed,
                                BeddingTypeInBedItem,
                                BeddingTypeInBedEditorDialog,
                                BeddingTypeInBedFinder)
        self.headerStrings = [self.tr('Bedding Types')]
