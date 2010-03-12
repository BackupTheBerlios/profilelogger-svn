from DataInProjectManagementItemModel import DataInProjectManagementItemModel

from PyQt4.QtGui import *

from Model.Facies import Facies
from Gui.ItemModels.FaciesItem import FaciesItem
from Gui.Dialogs.FaciesEditorDialog import FaciesEditorDialog

class FaciesItemModel(DataInProjectManagementItemModel):
    def __init__(self, parent):
        DataInProjectManagementItemModel.__init__(self, parent,
                                                  Facies,
                                                  FaciesItem,
                                                  FaciesEditorDialog,
                                                  Facies.name)
        self.headerStrings = [self.tr("Facies")]
