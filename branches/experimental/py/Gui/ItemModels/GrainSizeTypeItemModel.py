from DataManagementItemModel import DataManagementItemModel

from PyQt4.QtGui import *

from Model.GrainSizeType import GrainSizeType
from Gui.ItemModels.GrainSizeTypeItem import GrainSizeTypeItem
from Gui.Dialogs.GrainSizeTypeEditorDialog import GrainSizeTypeEditorDialog

class GrainSizeTypeItemModel(DataManagementItemModel):
    def __init__(self, parent):
        DataManagementItemModel.__init__(self, parent,
                                         GrainSizeType,
                                         GrainSizeTypeItem,
                                         GrainSizeTypeEditorDialog,
                                         GrainSizeType.name)
        self.headerStrings = [self.tr("Grain Size Types")]
