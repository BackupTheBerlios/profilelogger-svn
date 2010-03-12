from DataInBedManagementItemModel import DataInBedManagementItemModel

from PyQt4.QtGui import *

from Model.FossilInBed import FossilInBed
from Gui.ItemModels.FossilInBedItem import FossilInBedItem
from Gui.Dialogs.FossilInBedEditorDialog import FossilInBedEditorDialog

class FossilInBedItemModel(DataInBedManagementItemModel):
    def __init__(self, parent):
        DataInBedManagementItemModel.__init__(self, parent,
                                              FossilInBed,
                                              FossilInBedItem,
                                              FossilInBedEditorDialog,
                                              FossilInBed.id)
        self.headerStrings = [self.tr("Fossils")]
