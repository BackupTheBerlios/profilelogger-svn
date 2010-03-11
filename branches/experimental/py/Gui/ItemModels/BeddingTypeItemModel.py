from DataInProjectManagementItemModel import DataInProjectManagementItemModel

from PyQt4.QtGui import *

from Model.BeddingType import BeddingType
from Gui.ItemModels.BeddingTypeItem import BeddingTypeItem
from Gui.Dialogs.BeddingTypeEditorDialog import BeddingTypeEditorDialog

class BeddingTypeItemModel(DataInProjectManagementItemModel):
    def __init__(self, parent):
        DataInProjectManagementItemModel.__init__(self, parent,
                                                  BeddingType,
                                                  BeddingTypeItem,
                                                  BeddingTypeEditorDialog,
                                                  BeddingType.name)
        self.headerStrings = [self.tr("Bedding Types")]
