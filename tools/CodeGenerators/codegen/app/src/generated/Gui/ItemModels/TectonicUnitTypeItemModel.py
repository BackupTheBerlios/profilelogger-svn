from InProjectItemModel import *

from PyQt4.QtGui import *

from Model.TectonicUnitType import TectonicUnitType
from Gui.Dialogs.TectonicUnitTypeEditorDialog import TectonicUnitTypeEditorDialog

class TectonicUnitTypeItem(StandardItem):
    def __init__(self, entity):
        StandardItem.__init__(self, entity)
        self.showData()

class TectonicUnitTypeItemModel(InProjectItemModel):
    def __init__(self, parent):
        InProjectItemModel.__init__(self, parent,
                                    TectonicUnitType,
                                    TectonicUnitTypeItem,
                                    TectonicUnitTypeEditorDialog,
                                    TectonicUnitTypeFinder)
        self.headerStrings = [self.tr('Tectonic Unit Types')]
