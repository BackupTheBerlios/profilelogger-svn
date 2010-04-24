from InProjectItemModel import *

from PyQt4.QtGui import *

from Model.StratigraphicUnitType import StratigraphicUnitType
from Gui.Dialogs.StratigraphicUnitTypeEditorDialog import StratigraphicUnitTypeEditorDialog

class StratigraphicUnitTypeItem(StandardItem):
    def __init__(self, entity):
        StandardItem.__init__(self, entity)
        self.showData()

class StratigraphicUnitTypeItemModel(InProjectItemModel):
    def __init__(self, parent):
        InProjectItemModel.__init__(self, parent,
                                    StratigraphicUnitType,
                                    StratigraphicUnitTypeItem,
                                    StratigraphicUnitTypeEditorDialog,
                                    StratigraphicUnitTypeFinder)
        self.headerStrings = [self.tr('Stratigraphic Unit Types')]
