from DataManagementItemModel import DataManagementItemModel

from PyQt4.QtGui import *

from Model.TectonicUnit import TectonicUnit
from Gui.ItemModels.TectonicUnitItem import TectonicUnitItem
from Gui.Dialogs.TectonicUnitEditorDialog import TectonicUnitEditorDialog

class TectonicUnitItemModel(DataManagementItemModel):
    def __init__(self, parent):
        DataManagementItemModel.__init__(self, parent,
                                         TectonicUnit,
                                         TectonicUnitItem,
                                         TectonicUnitEditorDialog,
                                         TectonicUnit.name)
        self.headerStrings = [self.tr("Tectonic Units")]
