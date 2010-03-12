from DataInBedManagementItemModel import DataInBedManagementItemModel

from PyQt4.QtGui import *

from Model.LithologyInBed import LithologyInBed
from Gui.ItemModels.LithologyInBedItem import LithologyInBedItem
from Gui.Dialogs.LithologyInBedEditorDialog import LithologyInBedEditorDialog

class LithologyInBedItemModel(DataInBedManagementItemModel):
    def __init__(self, parent):
        DataInBedManagementItemModel.__init__(self, parent,
                                              LithologyInBed,
                                              LithologyInBedItem,
                                              LithologyInBedEditorDialog,
                                              LithologyInBed.id)
        self.headerStrings = [self.tr("Lithologies")]
