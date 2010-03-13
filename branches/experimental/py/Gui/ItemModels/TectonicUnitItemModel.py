from DataInProjectManagementItemModel import DataInProjectManagementItemModel

from PyQt4.QtGui import *

from Model.TectonicUnit import TectonicUnit
from Gui.ItemModels.TectonicUnitItem import TectonicUnitItem
from Gui.Dialogs.TectonicUnitEditorDialog import TectonicUnitEditorDialog

class TectonicUnitItemModel(DataInProjectManagementItemModel):
    def __init__(self, parent):
        DataInProjectManagementItemModel.__init__(self, parent,
                                                  TectonicUnit,
                                                  TectonicUnitItem,
                                                  TectonicUnitEditorDialog,
                                                  TectonicUnit.name)
        self.headerStrings = [self.tr("Tectonic Units")]
