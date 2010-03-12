from DataInBedManagementItemModel import DataInBedManagementItemModel

from PyQt4.QtGui import *

from Model.OutcropTypeInBed import OutcropTypeInBed
from Gui.ItemModels.OutcropTypeInBedItem import OutcropTypeInBedItem
from Gui.Dialogs.OutcropTypeInBedEditorDialog import OutcropTypeInBedEditorDialog

class OutcropTypeInBedItemModel(DataInBedManagementItemModel):
    def __init__(self, parent):
        DataInBedManagementItemModel.__init__(self, parent,
                                              OutcropTypeInBed,
                                              OutcropTypeInBedItem,
                                              OutcropTypeInBedEditorDialog,
                                              OutcropTypeInBed.id)
        self.headerStrings = [self.tr("Outcrop Types")]
