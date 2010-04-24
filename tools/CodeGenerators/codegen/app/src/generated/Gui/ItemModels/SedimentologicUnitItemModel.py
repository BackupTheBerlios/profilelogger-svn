from InProjectItemModel import *

from PyQt4.QtGui import *

from Model.SedimentologicUnit import SedimentologicUnit
from Gui.Dialogs.SedimentologicUnitEditorDialog import SedimentologicUnitEditorDialog

class SedimentologicUnitItem(StandardItem):
    def __init__(self, entity):
        StandardItem.__init__(self, entity)
        self.showData()

class SedimentologicUnitItemModel(InProjectItemModel):
    def __init__(self, parent):
        InProjectItemModel.__init__(self, parent,
                                    SedimentologicUnit,
                                    SedimentologicUnitItem,
                                    SedimentologicUnitEditorDialog,
                                    SedimentologicUnitFinder)
        self.headerStrings = [self.tr('Sedimentologic Units')]
