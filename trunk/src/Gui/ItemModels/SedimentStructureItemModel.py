from DataInProjectManagementItemModel import DataInProjectManagementItemModel

from PyQt4.QtGui import *

from Model.SedimentStructure import SedimentStructure
from Gui.ItemModels.SedimentStructureItem import SedimentStructureItem
from Gui.Dialogs.SedimentStructureEditorDialog import SedimentStructureEditorDialog

class SedimentStructureItemModel(DataInProjectManagementItemModel):
    def __init__(self, parent):
        DataInProjectManagementItemModel.__init__(self, parent,
                                                  SedimentStructure,
                                                  SedimentStructureItem,
                                                  SedimentStructureEditorDialog,
                                                  SedimentStructure.name)
        self.headerStrings = [self.tr("Sediment Structures")]
