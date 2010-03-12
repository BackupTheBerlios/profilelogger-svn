from DataManagementItemModel import DataManagementItemModel

from PyQt4.QtGui import *

from Model.StratigraphicUnitType import StratigraphicUnitType
from Gui.ItemModels.StratigraphicUnitTypeItem import StratigraphicUnitTypeItem
from Gui.Dialogs.StratigraphicUnitTypeEditorDialog import StratigraphicUnitTypeEditorDialog

class StratigraphicUnitTypeItemModel(DataManagementItemModel):
    def __init__(self, parent):
        DataManagementItemModel.__init__(self, parent,
                                         StratigraphicUnitType,
                                         StratigraphicUnitTypeItem,
                                         StratigraphicUnitTypeEditorDialog,
                                         StratigraphicUnitType.name)
        self.headerStrings = [self.tr("Stratigraphic Unit Types")]
