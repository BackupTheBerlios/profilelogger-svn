from DataInBedManagementItemModel import DataInBedManagementItemModel

from PyQt4.QtGui import *

from Model.FaciesInBed import FaciesInBed
from Gui.ItemModels.FaciesInBedItem import FaciesInBedItem
from Gui.Dialogs.FaciesInBedEditorDialog import FaciesInBedEditorDialog

class FaciesInBedItemModel(DataInBedManagementItemModel):
    def __init__(self, parent):
        DataInBedManagementItemModel.__init__(self, parent,
                                              FaciesInBed,
                                              FaciesInBedItem,
                                              FaciesInBedEditorDialog,
                                              FaciesInBed.id)
        self.headerStrings = [self.tr("Facies")]
