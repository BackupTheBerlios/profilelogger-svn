from InProjectItemModel import *

from PyQt4.QtGui import *

from Model.SedimentStructure import SedimentStructure
from Gui.Dialogs.SedimentStructureEditorDialog import SedimentStructureEditorDialog

class SedimentStructureItem(StandardItem):
    def __init__(self, entity):
        StandardItem.__init__(self, entity)
        self.showData()

class SedimentStructureItemModel(InProjectItemModel):
    def __init__(self, parent):
        InProjectItemModel.__init__(self, parent,
                                    SedimentStructure,
                                    SedimentStructureItem,
                                    SedimentStructureEditorDialog,
                                    SedimentStructureFinder)
        self.headerStrings = [self.tr('Sediment Structures')]
