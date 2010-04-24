from InProjectItemModel import *

from PyQt4.QtGui import *

from Model.OutcropType import OutcropType
from Gui.Dialogs.OutcropTypeEditorDialog import OutcropTypeEditorDialog

class OutcropTypeItem(StandardItem):
    def __init__(self, entity):
        StandardItem.__init__(self, entity)
        self.showData()

class OutcropTypeItemModel(InProjectItemModel):
    def __init__(self, parent):
        InProjectItemModel.__init__(self, parent,
                                    OutcropType,
                                    OutcropTypeItem,
                                    OutcropTypeEditorDialog,
                                    OutcropTypeFinder)
        self.headerStrings = [self.tr('Outcrop Types')]
