from InBedItemModel import *

from PyQt4.QtGui import *

from Model.OutcropTypeInBed import OutcropTypeInBed
from Gui.Dialogs.OutcropTypeInBedEditorDialog import OutcropTypeInBedEditorDialog

class OutcropTypeInBedItem(StandardItem):
    def __init__(self, entity):
        StandardItem.__init__(self, entity)
        self.showData()

class OutcropTypeInBedItemModel(InBedItemModel):
    def __init__(self, parent):
        InBedItemModel.__init__(self, parent,
                                OutcropTypeInBed,
                                OutcropTypeInBedItem,
                                OutcropTypeInBedEditorDialog,
                                OutcropTypeInBedFinder)
        self.headerStrings = [self.tr('Outcrop Types')]
