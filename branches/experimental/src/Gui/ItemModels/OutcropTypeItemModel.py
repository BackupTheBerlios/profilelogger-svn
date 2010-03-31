from DataInProjectManagementItemModel import DataInProjectManagementItemModel

from PyQt4.QtGui import *

from Model.OutcropType import OutcropType
from Gui.ItemModels.OutcropTypeItem import OutcropTypeItem
from Gui.Dialogs.OutcropTypeEditorDialog import OutcropTypeEditorDialog

class OutcropTypeItemModel(DataInProjectManagementItemModel):
    def __init__(self, parent):
        DataInProjectManagementItemModel.__init__(self, parent,
                                                  OutcropType,
                                                  OutcropTypeItem,
                                                  OutcropTypeEditorDialog,
                                                  OutcropType.name)
        self.headerStrings = [self.tr("Outcrop Types")]
