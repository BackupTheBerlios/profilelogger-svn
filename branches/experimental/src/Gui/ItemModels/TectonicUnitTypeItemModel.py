from DataManagementItemModel import DataManagementItemModel

from PyQt4.QtGui import *

from Model.TectonicUnitType import TectonicUnitType
from Gui.ItemModels.TectonicUnitTypeItem import TectonicUnitTypeItem
from Gui.Dialogs.TectonicUnitTypeEditorDialog import TectonicUnitTypeEditorDialog

class TectonicUnitTypeItemModel(DataManagementItemModel):
    def __init__(self, parent):
        DataManagementItemModel.__init__(self, parent,
                                         TectonicUnitType,
                                         TectonicUnitTypeItem,
                                         TectonicUnitTypeEditorDialog,
                                         TectonicUnitType.name)
        self.headerStrings = [self.tr("Tectonic Unit Types")]
