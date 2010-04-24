from InBedItemModel import *

from PyQt4.QtGui import *

from Model.FaciesInBed import FaciesInBed
from Gui.Dialogs.FaciesInBedEditorDialog import FaciesInBedEditorDialog

class FaciesInBedItem(StandardItem):
    def __init__(self, entity):
        StandardItem.__init__(self, entity)
        self.showData()

class FaciesInBedItemModel(InBedItemModel):
    def __init__(self, parent):
        InBedItemModel.__init__(self, parent,
                                FaciesInBed,
                                FaciesInBedItem,
                                FaciesInBedEditorDialog,
                                FaciesInBedFinder)
        self.headerStrings = [self.tr('Facies')]
