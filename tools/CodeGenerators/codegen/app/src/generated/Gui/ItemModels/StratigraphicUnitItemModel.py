from InProjectItemModel import *

from PyQt4.QtGui import *

from Model.StratigraphicUnit import StratigraphicUnit
from Gui.Dialogs.StratigraphicUnitEditorDialog import StratigraphicUnitEditorDialog

class StratigraphicUnitItem(StandardItem):
    def __init__(self, entity):
        StandardItem.__init__(self, entity)
        self.showData()

class StratigraphicUnitItemModel(InProjectItemModel):
    def __init__(self, parent):
        InProjectItemModel.__init__(self, parent,
                                    StratigraphicUnit,
                                    StratigraphicUnitItem,
                                    StratigraphicUnitEditorDialog,
                                    StratigraphicUnitFinder)
        self.headerStrings = [self.tr('Stratigraphic Units')]
