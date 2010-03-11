from DataManagementItemModel import DataManagementItemModel

from PyQt4.QtGui import *

from Model.GrainSize import GrainSize
from Gui.ItemModels.GrainSizeItem import GrainSizeItem
from Gui.Dialogs.GrainSizeEditorDialog import GrainSizeEditorDialog

class GrainSizeItemModel(DataManagementItemModel):
    def __init__(self, parent):
        DataManagementItemModel.__init__(self, parent,
                                         GrainSize,
                                         GrainSizeItem,
                                         GrainSizeEditorDialog,
                                         GrainSize.name)
        self.headerStrings = [self.tr("Grain Sizes")]
