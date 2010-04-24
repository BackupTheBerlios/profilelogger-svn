from InProjectItemModel import *

from PyQt4.QtGui import *

from Model.SedimentologicUnitType import SedimentologicUnitType
from Gui.Dialogs.SedimentologicUnitTypeEditorDialog import SedimentologicUnitTypeEditorDialog

class SedimentologicUnitTypeItem(StandardItem):
    def __init__(self, entity):
        StandardItem.__init__(self, entity)
        self.showData()

class SedimentologicUnitTypeItemModel(InProjectItemModel):
    def __init__(self, parent):
        InProjectItemModel.__init__(self, parent,
                                    SedimentologicUnitType,
                                    SedimentologicUnitTypeItem,
                                    SedimentologicUnitTypeEditorDialog,
                                    SedimentologicUnitTypeFinder)
        self.headerStrings = [self.tr('Sedimentologic Unit Types')]
