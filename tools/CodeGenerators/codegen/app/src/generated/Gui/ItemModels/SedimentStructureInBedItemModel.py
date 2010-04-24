from InBedItemModel import *

from PyQt4.QtGui import *

from Model.SedimentStructureInBed import SedimentStructureInBed
from Gui.Dialogs.SedimentStructureInBedEditorDialog import SedimentStructureInBedEditorDialog

class SedimentStructureInBedItem(StandardItem):
    def __init__(self, entity):
        StandardItem.__init__(self, entity)
        self.showData()

class SedimentStructureInBedItemModel(InBedItemModel):
    def __init__(self, parent):
        InBedItemModel.__init__(self, parent,
                                SedimentStructureInBed,
                                SedimentStructureInBedItem,
                                SedimentStructureInBedEditorDialog,
                                SedimentStructureInBedFinder)
        self.headerStrings = [self.tr('Sediment Structures')]
