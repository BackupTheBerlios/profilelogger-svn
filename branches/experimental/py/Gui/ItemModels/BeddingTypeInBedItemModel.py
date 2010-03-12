from DataInBedManagementItemModel import DataInBedManagementItemModel

from PyQt4.QtGui import *

from Model.BeddingTypeInBed import BeddingTypeInBed
from Gui.ItemModels.BeddingTypeInBedItem import BeddingTypeInBedItem
from Gui.Dialogs.BeddingTypeInBedEditorDialog import BeddingTypeInBedEditorDialog

class BeddingTypeInBedItemModel(DataInBedManagementItemModel):
    def __init__(self, parent):
        DataInBedManagementItemModel.__init__(self, parent,
                                              BeddingTypeInBed,
                                              BeddingTypeInBedItem,
                                              BeddingTypeInBedEditorDialog,
                                              BeddingTypeInBed.id)
        self.headerStrings = [self.tr("Bedding Types")]
