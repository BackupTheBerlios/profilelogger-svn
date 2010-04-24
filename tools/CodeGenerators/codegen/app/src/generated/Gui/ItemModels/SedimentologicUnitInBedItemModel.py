from InBedItemModel import *

from PyQt4.QtGui import *

from Model.SedimentologicUnitInBed import SedimentologicUnitInBed
from Gui.Dialogs.SedimentologicUnitInBedEditorDialog import SedimentologicUnitInBedEditorDialog

class SedimentologicUnitInBedItem(StandardItem):
    def __init__(self, entity):
        StandardItem.__init__(self, entity)
        self.showData()

class SedimentologicUnitInBedItemModel(InBedItemModel):
    def __init__(self, parent):
        InBedItemModel.__init__(self, parent,
                                SedimentologicUnitInBed,
                                SedimentologicUnitInBedItem,
                                SedimentologicUnitInBedEditorDialog,
                                SedimentologicUnitInBedFinder)
        self.headerStrings = [self.tr('Sedimentologic Units')]
