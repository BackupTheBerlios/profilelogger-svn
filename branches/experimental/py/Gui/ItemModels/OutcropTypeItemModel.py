from DataManagementItemModel import DataManagementItemModel

from PyQt4.QtGui import *

from Model.OutcropType import OutcropType
from Gui.ItemModels.OutcropTypeItem import OutcropTypeItem
from Gui.Dialogs.OutcropTypeEditorDialog import OutcropTypeEditorDialog

class OutcropTypeItemModel(DataManagementItemModel):
    def __init__(self, parent):
        DataManagementItemModel.__init__(self, parent,
                                         OutcropType,
                                         OutcropTypeItem,
                                         OutcropTypeEditorDialog,
                                         OutcropType.name)
        self.headerStrings = [self.tr("Outcrop Types")]
