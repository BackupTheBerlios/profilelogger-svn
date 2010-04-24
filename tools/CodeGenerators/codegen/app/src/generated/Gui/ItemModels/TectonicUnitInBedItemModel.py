from InBedItemModel import *

from PyQt4.QtGui import *

from Model.TectonicUnitInBed import TectonicUnitInBed
from Gui.Dialogs.TectonicUnitInBedEditorDialog import TectonicUnitInBedEditorDialog

class TectonicUnitInBedItem(StandardItem):
    def __init__(self, entity):
        StandardItem.__init__(self, entity)
        self.showData()

class TectonicUnitInBedItemModel(InBedItemModel):
    def __init__(self, parent):
        InBedItemModel.__init__(self, parent,
                                TectonicUnitInBed,
                                TectonicUnitInBedItem,
                                TectonicUnitInBedEditorDialog,
                                TectonicUnitInBedFinder)
        self.headerStrings = [self.tr('Tectonic Units')]
