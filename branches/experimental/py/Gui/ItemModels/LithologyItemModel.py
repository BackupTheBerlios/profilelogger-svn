from DataInProjectManagementItemModel import DataInProjectManagementItemModel

from PyQt4.QtGui import *

from Model.Lithology import Lithology
from Gui.ItemModels.LithologyItem import LithologyItem
from Gui.Dialogs.LithologyEditorDialog import LithologyEditorDialog

class LithologyItemModel(DataInProjectManagementItemModel):
    def __init__(self, parent):
        DataInProjectManagementItemModel.__init__(self, parent,
                                                  Lithology,
                                                  LithologyItem,
                                                  LithologyEditorDialog,
                                                  Lithology.name)
        self.headerStrings = [self.tr("Lithologies")]
