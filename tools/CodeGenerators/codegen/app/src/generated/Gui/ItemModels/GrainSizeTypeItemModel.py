from InProjectItemModel import *

from PyQt4.QtGui import *

from Model.GrainSizeType import GrainSizeType
from Gui.Dialogs.GrainSizeTypeEditorDialog import GrainSizeTypeEditorDialog

class GrainSizeTypeItem(StandardItem):
    def __init__(self, entity):
        StandardItem.__init__(self, entity)
        self.showData()

class GrainSizeTypeItemModel(InProjectItemModel):
    def __init__(self, parent):
        InProjectItemModel.__init__(self, parent,
                                    GrainSizeType,
                                    GrainSizeTypeItem,
                                    GrainSizeTypeEditorDialog,
                                    GrainSizeTypeFinder)
        self.headerStrings = [self.tr('Grain Size Types')]
