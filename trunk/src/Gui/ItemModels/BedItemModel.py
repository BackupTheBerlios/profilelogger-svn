from DataInProfileManagementItemModel import DataInProfileManagementItemModel

from PyQt4.QtGui import *

from Model.Bed import Bed
from Gui.ItemModels.BedItem import BedItem
from Gui import *

class BedItemModel(DataInProfileManagementItemModel):
    def __init__(self, parent):
        DataInProfileManagementItemModel.__init__(self, parent,
                                                  Bed,
                                                  BedItem,
                                                  Dialogs.BedEditorDialog.BedEditorDialog,
                                                  Bed.name)
        self.headerStrings = [self.tr("Beds")]
