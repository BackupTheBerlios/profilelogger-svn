from InProjectItemModel import *

from PyQt4.QtGui import *

from Model.GrainSize import GrainSize
from Gui.Dialogs.GrainSizeEditorDialog import GrainSizeEditorDialog

class GrainSizeItem(StandardItem):
    def __init__(self, entity):
        StandardItem.__init__(self, entity)
        self.showData()

class GrainSizeItemModel(InProjectItemModel):
    def __init__(self, parent):
        InProjectItemModel.__init__(self, parent,
                                    GrainSize,
                                    GrainSizeItem,
                                    GrainSizeEditorDialog,
                                    GrainSizeFinder)
        self.headerStrings = [self.tr('Grain Sizes')]
