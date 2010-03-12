from DataInBedManagementItemModel import DataInBedManagementItemModel

from PyQt4.QtGui import *

from Model.GrainSizeInBed import GrainSizeInBed
from Gui.ItemModels.GrainSizeInBedItem import GrainSizeInBedItem
from Gui.Dialogs.GrainSizeInBedEditorDialog import GrainSizeInBedEditorDialog

class GrainSizeInBedItemModel(DataInBedManagementItemModel):
    def __init__(self, parent):
        DataInBedManagementItemModel.__init__(self, parent,
                                              GrainSizeInBed,
                                              GrainSizeInBedItem,
                                              GrainSizeInBedEditorDialog,
                                              GrainSizeInBed.id)
        self.headerStrings = [self.tr("Grain Sizes")]
