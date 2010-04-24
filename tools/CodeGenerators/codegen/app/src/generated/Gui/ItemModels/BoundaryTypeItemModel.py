from InProjectItemModel import *

from PyQt4.QtGui import *

from Model.BoundaryType import BoundaryType
from Gui.Dialogs.BoundaryTypeEditorDialog import BoundaryTypeEditorDialog

class BoundaryTypeItem(StandardItem):
    def __init__(self, entity):
        StandardItem.__init__(self, entity)
        self.showData()

class BoundaryTypeItemModel(InProjectItemModel):
    def __init__(self, parent):
        InProjectItemModel.__init__(self, parent,
                                    BoundaryType,
                                    BoundaryTypeItem,
                                    BoundaryTypeEditorDialog,
                                    BoundaryTypeFinder)
        self.headerStrings = [self.tr('Boundary Types')]
