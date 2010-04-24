from InProjectItemModel import *

from PyQt4.QtGui import *

from Model.TectonicUnit import TectonicUnit
from Gui.Dialogs.TectonicUnitEditorDialog import TectonicUnitEditorDialog

class TectonicUnitItem(StandardItem):
    def __init__(self, entity):
        StandardItem.__init__(self, entity)
        self.showData()

class TectonicUnitItemModel(InProjectItemModel):
    def __init__(self, parent):
        InProjectItemModel.__init__(self, parent,
                                    TectonicUnit,
                                    TectonicUnitItem,
                                    TectonicUnitEditorDialog,
                                    TectonicUnitFinder)
        self.headerStrings = [self.tr('Tectonic Units')]
