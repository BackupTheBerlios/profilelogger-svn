from DataInBedManagementItemModel import DataInBedManagementItemModel

from PyQt4.QtGui import *

from Model.TectonicUnitInBed import TectonicUnitInBed
from Gui.ItemModels.TectonicUnitInBedItem import TectonicUnitInBedItem
from Gui.Dialogs.TectonicUnitInBedEditorDialog import TectonicUnitInBedEditorDialog

class TectonicUnitInBedItemModel(DataInBedManagementItemModel):
    def __init__(self, parent):
        DataInBedManagementItemModel.__init__(self, parent,
                                              TectonicUnitInBed,
                                              TectonicUnitInBedItem,
                                              TectonicUnitInBedEditorDialog,
                                              TectonicUnitInBed.id)
        self.headerStrings = [self.tr("Tectonic Units")]
