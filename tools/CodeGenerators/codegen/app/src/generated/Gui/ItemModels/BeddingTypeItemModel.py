from InProjectItemModel import *

from PyQt4.QtGui import *

from Model.BeddingType import BeddingType
from Gui.Dialogs.BeddingTypeEditorDialog import BeddingTypeEditorDialog

class BeddingTypeItem(StandardItem):
    def __init__(self, entity):
        StandardItem.__init__(self, entity)
        self.showData()

class BeddingTypeItemModel(InProjectItemModel):
    def __init__(self, parent):
        InProjectItemModel.__init__(self, parent,
                                    BeddingType,
                                    BeddingTypeItem,
                                    BeddingTypeEditorDialog,
                                    BeddingTypeFinder)
        self.headerStrings = [self.tr('Bedding Types')]
