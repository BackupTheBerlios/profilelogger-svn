from DataInProjectManagementItemModel import DataInProjectManagementItemModel

from PyQt4.QtGui import *

from Model.StratigraphicUnit import StratigraphicUnit
from Gui.ItemModels.StratigraphicUnitItem import StratigraphicUnitItem
from Gui.Dialogs.StratigraphicUnitEditorDialog import StratigraphicUnitEditorDialog

class StratigraphicUnitItemModel(DataInProjectManagementItemModel):
    def __init__(self, parent):
        DataInProjectManagementItemModel.__init__(self, parent,
                                                  StratigraphicUnit,
                                                  StratigraphicUnitItem,
                                                  StratigraphicUnitEditorDialog,
                                                  StratigraphicUnit.name)
        self.headerStrings = [self.tr("Stratigraphic Units")]
