from InBedItemModel import *

from PyQt4.QtGui import *

from Model.BoundaryTypeInBed import BoundaryTypeInBed
from Gui.Dialogs.BoundaryTypeInBedEditorDialog import BoundaryTypeInBedEditorDialog

class BoundaryTypeInBedItem(StandardItem):
    def __init__(self, entity):
        StandardItem.__init__(self, entity)
        self.showData()

class BoundaryTypeInBedItemModel(InBedItemModel):
    def __init__(self, parent):
        InBedItemModel.__init__(self, parent,
                                BoundaryTypeInBed,
                                BoundaryTypeInBedItem,
                                BoundaryTypeInBedEditorDialog,
                                BoundaryTypeInBedFinder)
        self.headerStrings = [self.tr('Boundary Types')]
