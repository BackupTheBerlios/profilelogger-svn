from DataInProjectManagementItemModel import DataInProjectManagementItemModel

from PyQt4.QtGui import *

from Model.BoundaryType import BoundaryType
from Gui.ItemModels.BoundaryTypeItem import BoundaryTypeItem
from Gui.Dialogs.BoundaryTypeEditorDialog import BoundaryTypeEditorDialog

class BoundaryTypeItemModel(DataInProjectManagementItemModel):
    def __init__(self, parent):
        DataInProjectManagementItemModel.__init__(self, parent,
                                                  BoundaryType,
                                                  BoundaryTypeItem,
                                                  BoundaryTypeEditorDialog,
                                                  BoundaryType.name)
        self.headerStrings = [self.tr("Boundary Types")]
