from DataInBedManagementItemModel import DataInBedManagementItemModel

from PyQt4.QtGui import *

from Model.SedimentStructureInBed import SedimentStructureInBed
from Gui.ItemModels.SedimentStructureInBedItem import SedimentStructureInBedItem
from Gui.Dialogs.SedimentStructureInBedEditorDialog import SedimentStructureInBedEditorDialog

class SedimentStructureInBedItemModel(DataInBedManagementItemModel):
    def __init__(self, parent):
        DataInBedManagementItemModel.__init__(self, parent,
                                              SedimentStructureInBed,
                                              SedimentStructureInBedItem,
                                              SedimentStructureInBedEditorDialog,
                                              SedimentStructureInBed.id)
        self.headerStrings = [self.tr("Sediment Structures")]
