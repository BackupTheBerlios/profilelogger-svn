from DataInBedManagementItemModel import DataInBedManagementItemModel

from PyQt4.QtGui import *

from Model.LithologicalUnitInBed import LithologicalUnitInBed
from Gui.ItemModels.LithologicalUnitInBedItem import LithologicalUnitInBedItem
from Gui.Dialogs.LithologicalUnitInBedEditorDialog import LithologicalUnitInBedEditorDialog

class LithologicalUnitInBedItemModel(DataInBedManagementItemModel):
    def __init__(self, parent):
        DataInBedManagementItemModel.__init__(self, parent,
                                              LithologicalUnitInBed,
                                              LithologicalUnitInBedItem,
                                              LithologicalUnitInBedEditorDialog,
                                              LithologicalUnitInBed.id)
        self.headerStrings = [self.tr("Lithological Units")]
