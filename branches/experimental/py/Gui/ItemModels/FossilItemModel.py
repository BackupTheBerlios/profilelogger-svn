from DataInProjectManagementItemModel import DataInProjectManagementItemModel

from PyQt4.QtGui import *

from Model.Fossil import Fossil
from Gui.ItemModels.FossilItem import FossilItem
from Gui.Dialogs.FossilEditorDialog import FossilEditorDialog

class FossilItemModel(DataInProjectManagementItemModel):
    def __init__(self, parent):
        DataInProjectManagementItemModel.__init__(self, parent,
                                                  Fossil,
                                                  FossilItem,
                                                  FossilEditorDialog,
                                                  Fossil.name)
        self.headerStrings = [self.tr("Fossils")]
