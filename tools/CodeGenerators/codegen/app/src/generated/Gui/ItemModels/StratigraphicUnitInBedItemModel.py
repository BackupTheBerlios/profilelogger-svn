from InBedItemModel import *

from PyQt4.QtGui import *

from Model.StratigraphicUnitInBed import StratigraphicUnitInBed
from Gui.Dialogs.StratigraphicUnitInBedEditorDialog import StratigraphicUnitInBedEditorDialog

class StratigraphicUnitInBedItem(StandardItem):
    def __init__(self, entity):
        StandardItem.__init__(self, entity)
        self.showData()

class StratigraphicUnitInBedItemModel(InBedItemModel):
    def __init__(self, parent):
        InBedItemModel.__init__(self, parent,
                                StratigraphicUnitInBed,
                                StratigraphicUnitInBedItem,
                                StratigraphicUnitInBedEditorDialog,
                                StratigraphicUnitInBedFinder)
        self.headerStrings = [self.tr('Stratigraphic Units')]
