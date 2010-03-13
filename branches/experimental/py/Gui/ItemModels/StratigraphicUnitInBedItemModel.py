from DataInBedManagementItemModel import DataInBedManagementItemModel

from PyQt4.QtGui import *

from Model.StratigraphicUnitInBed import StratigraphicUnitInBed
from Gui.ItemModels.StratigraphicUnitInBedItem import StratigraphicUnitInBedItem
from Gui.Dialogs.StratigraphicUnitInBedEditorDialog import StratigraphicUnitInBedEditorDialog

class StratigraphicUnitInBedItemModel(DataInBedManagementItemModel):
    def __init__(self, parent):
        DataInBedManagementItemModel.__init__(self, parent,
                                              StratigraphicUnitInBed,
                                              StratigraphicUnitInBedItem,
                                              StratigraphicUnitInBedEditorDialog,
                                              StratigraphicUnitInBed.id)
        self.headerStrings = [self.tr("Stratigraphic Units")]
