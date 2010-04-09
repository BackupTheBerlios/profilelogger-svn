from DataInBedManagementItemModel import DataInBedManagementItemModel

from PyQt4.QtGui import *

from Model.BoundaryTypeInBed import BoundaryTypeInBed
from Gui.ItemModels.BoundaryTypeInBedItem import BoundaryTypeInBedItem
from Gui.Dialogs.BoundaryTypeInBedEditorDialog import BoundaryTypeInBedEditorDialog

class BoundaryTypeInBedItemModel(DataInBedManagementItemModel):
    def __init__(self, parent):
        DataInBedManagementItemModel.__init__(self, parent,
                                              BoundaryTypeInBed,
                                              BoundaryTypeInBedItem,
                                              BoundaryTypeInBedEditorDialog,
                                              BoundaryTypeInBed.id)
        self.headerStrings = [self.tr("Boundary Types")]
